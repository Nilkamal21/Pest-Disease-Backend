import torch
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v2
from PIL import Image
import os
import argparse

# Import the recommendation function
from recommendation import get_recommendation

# Absolute paths - update if needed
MODEL_PATH = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\models\saved_models\plant_disease_classifier.pth'
CLASS_NAMES_PATH = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\data\processed\train'
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load class names from train folder
class_names = sorted([d for d in os.listdir(CLASS_NAMES_PATH) if os.path.isdir(os.path.join(CLASS_NAMES_PATH, d))])
NUM_CLASSES = len(class_names)

# Prepare Image Transform (same as training validation)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

# Load Model
model = mobilenet_v2(weights=None)
model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, NUM_CLASSES)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.to(DEVICE)
model.eval()

def predict(image_path):
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(input_tensor)
    _, predicted_idx = torch.max(outputs, 1)
    predicted_class = class_names[predicted_idx.item()]
    return predicted_class

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plant Disease Classification Inference with Recommendations")
    parser.add_argument("image_path", type=str, help="Path to an input image")
    args = parser.parse_args()

    predicted_class = predict(args.image_path)
    print(f"Predicted Disease Class: {predicted_class}")

    recommendation = get_recommendation(predicted_class)
    print("\n--- Treatment Recommendation ---")
    for key, value in recommendation.items():
        print(f"{key.capitalize()}: {value}")
