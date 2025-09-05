import os
import shutil
import uuid
from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
from torchvision.models import mobilenet_v2
import torch.nn as nn
import torchvision.transforms as transforms
from recommendation import get_recommendation  # Your recommendations module
from gtts import gTTS

# Absolute paths - update if needed
MODEL_PATH = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\models\saved_models\plant_disease_classifier.pth'
CLASS_NAMES_PATH = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\data\processed\train'

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class_names = sorted([d for d in os.listdir(CLASS_NAMES_PATH) if os.path.isdir(os.path.join(CLASS_NAMES_PATH, d))])
NUM_CLASSES = len(class_names)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

def load_model():
    model = mobilenet_v2(pretrained=False)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, NUM_CLASSES)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()
    return model


model = load_model()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify frontend origins explicitly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = "temp_files"
os.makedirs(TEMP_DIR, exist_ok=True)

def predict_disease(image_path, model):
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(input_tensor)
    _, predicted_idx = torch.max(outputs, 1)
    return class_names[predicted_idx.item()]

def generate_tts(text: str, lang: str) -> str:
    # gTTS does not support Punjabi ('pa'), fallback to Hindi ('hi')
    tts_lang = lang if lang in ['en', 'hi', 'bn'] else 'hi'
    tts = gTTS(text=text, lang=tts_lang)
    filename = f"{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(TEMP_DIR, filename)
    tts.save(filepath)
    return filepath

@app.post("/predict/")
async def predict(
    image: UploadFile = File(...),
    language: str = Form(...),
    user_text: Optional[str] = Form(None)
):
    # Save image temporarily
    image_path = os.path.join(TEMP_DIR, image.filename)
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Predict disease
    predicted_class = predict_disease(image_path, model)

    # Get recommendation for predicted disease and language
    recommendation = get_recommendation(predicted_class, language)

    # Generate TTS audio file for advice text
    advice_text = recommendation.get('advice', '')
    tts_filepath = generate_tts(advice_text, language)
    tts_filename = os.path.basename(tts_filepath)

    # Optional: remove uploaded image to save space
    # os.remove(image_path)

    return JSONResponse(content={
        "recognized_text": user_text or "",
        "predicted_class": predicted_class.replace('_', ' '),
        "recommendation": recommendation,
        "tts_audio_url": f"/tts/{tts_filename}"
    })

@app.get("/tts/{filename}")
async def get_tts_audio(filename: str):
    file_path = os.path.join(TEMP_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg", filename=filename)
    return JSONResponse(content={"error": "Audio file not found"}, status_code=404)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
