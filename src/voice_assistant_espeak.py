import os
import queue
import json
import sounddevice as sd
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v2
import torch
from recommendation import get_recommendation
from gtts import gTTS
import uuid
import pygame

# Paths - update as needed
VOSK_MODEL_PATH = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\models\vosk_hi'
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

pygame.mixer.init()


def load_model():
    model = mobilenet_v2(weights=None)
    model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, NUM_CLASSES)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()
    return model


def predict_disease(image_path, model):
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(input_tensor)
    _, predicted_idx = torch.max(outputs, 1)
    return class_names[predicted_idx.item()]


def generate_and_play_tts(text, lang):
    tts_lang = 'en' if lang not in ['en', 'hi', 'bn', 'pa'] else lang
    # gTTS does not directly support 'pa' (Punjabi), fallback to 'en' or 'hi'
    if lang == 'pa':
        tts_lang = 'hi'  # best alternative for Punjabi
    tts = gTTS(text=text, lang=tts_lang)
    filename = f"tts_{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    os.remove(filename)


def speak(text, lang):
    print(text)
    generate_and_play_tts(text, lang)


def recognize_speech(model_path, duration=7, samplerate=16000):
    import vosk
    q = queue.Queue()

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Vosk model not found at {model_path}")

    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, samplerate)
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("Listening for voice input...")
        text = ""
        for _ in range(int(duration * samplerate / 8000)):
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text += " " + result.get("text", "")
        final_result = json.loads(rec.FinalResult())
        text += " " + final_result.get("text", "")
        return text.strip()


class PlantDiseaseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plant Disease Detection Assistant")
        self.geometry("720x800")
        self.selected_lang = 'en'
        self.model = load_model()
        self.img_path = None
        self.disease_class = None

        # Translation dictionary extended to include Punjabi ('pa')
        self.translations = {
            'en': {
                'select_language': 'Select Language:',
                'choose_image': 'Choose Image',
                'capture_image': 'Capture Image',
                'speak_problem': 'Speak Problem',
                'type_problem': 'Type Problem',
                'submit': 'Submit',
                'recommendation': 'Recommendation',
                'additional_info': 'Additional Information (Optional):',
                'need_more_tips': 'Would you like some additional tips on pesticide safety? Say yes or no.',
                'yes': ['yes', 'ya'],
                'no': ['no', 'n'],
                'pesticide_safety_tips': 'Always wear gloves and masks when applying pesticides. Store chemicals safely away from children.',
                'thank_you': 'Thank you for using the plant disease assistant. Stay safe and healthy!',
                'invalid_choice': 'Invalid choice. Please try again.',
                'error_camera': "Unable to access camera.",
                'capturing': "Look at the camera. Capturing image in 5 seconds.",
                'pesticides': 'Pesticides',
                'fertilizers': 'Fertilizers',
                'dosage': 'Dosage',
            },
            'hi': {
                'select_language': 'भाषा चुनें:',
                'choose_image': 'छवि चुनें',
                'capture_image': 'कैमरा से फोटो लें',
                'speak_problem': 'समस्या बोलें',
                'type_problem': 'समस्या लिखें',
                'submit': 'जमा करें',
                'recommendation': 'सिफारिश',
                'additional_info': 'अतिरिक्त जानकारी (वैकल्पिक):',
                'need_more_tips': 'क्या आप कीटनाशक सुरक्षा पर कुछ अतिरिक्त सुझाव चाहते हैं? कृपया हाँ या नहीं कहें।',
                'yes': ['हाँ', 'हाँ'],
                'no': ['नहीं', 'ना'],
                'pesticide_safety_tips': 'कीटनाशक प्रयोग के दौरान हमेशा दस्ताने और मास्क पहनें। रसायनों को बच्चों से दूर सुरक्षित रखें।',
                'thank_you': 'पादप रोग सहायक का उपयोग करने के लिए धन्यवाद। सुरक्षित और स्वस्थ रहें!',
                'invalid_choice': 'अमान्य विकल्प। कृपया पुनः प्रयास करें।',
                'error_camera': "कैमरे तक पहुंच संभव नहीं है।",
                'capturing': "कैमरा की ओर देखें। ५ सेकंड में फोटो लिया जाएगा।",
                'pesticides': 'कीटनाशक',
                'fertilizers': 'उर्वरक',
                'dosage': 'खुराक',
            },
            'bn': {
                'select_language': 'ভাষা নির্বাচন করুন:',
                'choose_image': 'ছবি নির্বাচন করুন',
                'capture_image': 'ক্যামেরা থেকে ছবি নিন',
                'speak_problem': 'সমস্যা বলুন',
                'type_problem': 'সমস্যা লিখুন',
                'submit': 'জমা দিন',
                'recommendation': 'প্রস্তাব',
                'additional_info': 'অতিরিক্ত তথ্য (ঐচ্ছিক):',
                'need_more_tips': 'আপনি কি কীটনাশক নিরাপত্তা সম্পর্কে অতিরিক্ত পরামর্শ চান? হ্যাঁ বা না বলুন।',
                'yes': ['হ্যাঁ', 'হ্যাঁ'],
                'no': ['না', 'না'],
                'pesticide_safety_tips': 'কীটনাশক প্রয়োগের সময় সর্বদা দস্তানা এবং মাস্ক পরুন। রাসায়নিকগুলি শিশুদের হাত থেকে দূরে সুরক্ষিত রাখুন।',
                'thank_you': 'গাছের রোগ সহায়ক ব্যবহারের জন্য ধন্যবাদ। নিরাপদে থাকুন এবং সুস্থ থাকুন!',
                'invalid_choice': 'ভুল নির্বাচন। অনুগ্রহ করে আবার চেষ্টা করুন।',
                'error_camera': "ক্যামেরায় অ্যাক্সেস পাওয়া যায়নি।",
                'capturing': "ক্যামেরার দিকে তাকান। ৫ সেকেন্ডে ছবি তোলা হবে।",
                'pesticides': 'কীটনাশক',
                'fertilizers': 'সার',
                'dosage': 'মাত্রা',
            },
            'pa': {
                'select_language': 'ਭਾਸ਼ਾ ਚੁਣੋ:',
                'choose_image': 'ਚਿੱਤਰ ਚੁਣੋ',
                'capture_image': 'ਕੈਮਰੇ ਨਾਲ ਤਸਵੀਰ ਲਓ',
                'speak_problem': 'ਮੁੱਦੇ ਬੋਲੋ',
                'type_problem': 'ਮੁੱਦਾ ਲਿਖੋ',
                'submit': 'ਜਮ੍ਹਾਂ ਕਰੋ',
                'recommendation': 'ਸਿਫ਼ਾਰਿਸ਼',
                'additional_info': 'ਵਿਕਲਪਿਕ ਵਾਧੂ ਜਾਣਕਾਰੀ:',
                'need_more_tips': 'ਕੀ ਤੁਸੀਂ ਕੀਟਨਾਸ਼ਕ ਸੁਰੱਖਿਆ ਬਾਰੇ ਵਾਧੂ ਸੂਝਵਾਂ ਲੈਣਾ ਚਾਹੁੰਦੇ ਹੋ? ਹਾਂ ਜਾਂ ਨਾ ਕਹੋ।',
                'yes': ['ਹਾਂ', 'ਹਾਂ'],
                'no': ['ਨ੍ਹੀਂ', 'ਨਾ'],
                'pesticide_safety_tips': 'ਕੀਟਨਾਸ਼ਕ ਲਾਉਂਦੇ ਸਮੇਂ ਹਮੇਸ਼ਾਂ ਦਸਤਾਨੇ ਅਤੇ ਮਾਸਕ ਪਹਿਨੋ। ਰਸਾਇਣ ਬੱਚਿਆਂ ਤੋਂ ਦੂਰ ਰੱਖੋ।',
                'thank_you': 'ਪੌਧੇ ਰੋਗ ਸਹਾਇਕ ਵਰਤਣ ਲਈ ਧੰਨਵਾਦ। ਸੁਰੱਖਿਅਤ ਅਤੇ ਤੰਦਰੁਸਤ ਰਹੋ!',
                'invalid_choice': 'ਗਲਤ ਚੋਣ। ਕਿਰਪਾ ਕਰਕੇ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।',
                'error_camera': 'ਕੈਮਰੇ ਤੱਕ ਪਹੁੰਚ ਨਹੀੰ ਹੋਈ।',
                'capturing': 'ਕੈਮਰੇ ਵੱਲ ਵੇਖੋ। 5 ਸਕਿੰਟਾਂ ਵਿੱਚ ਤਸਵੀਰ ਲਵਾਈ ਜਾਵੇਗੀ।',
                'pesticides': 'ਕੀਟਨਾਸ਼ਕ',
                'fertilizers': 'ਖਾਦ',
                'dosage': 'ਮਾਤਰਾ',
            }
        }

        # Language selector UI including Punjabi
        self.lang_var = tk.StringVar(value='en')
        lang_label = tk.Label(self, text=self.translations['en']['select_language'], font=('Arial', 14))
        lang_label.pack(pady=5)
        lang_menu = tk.OptionMenu(self, self.lang_var, *self.translations.keys(), command=self.change_language)
        lang_menu.pack()

        # Image display area
        self.img_label = tk.Label(self)
        self.img_label.pack(pady=10)

        # Buttons frame
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        self.btn_choose = tk.Button(btn_frame, text=self.translations['en']['choose_image'], command=self.choose_image)
        self.btn_choose.grid(row=0, column=0, padx=5)

        self.btn_capture = tk.Button(btn_frame, text=self.translations['en']['capture_image'], command=self.capture_image)
        self.btn_capture.grid(row=0, column=1, padx=5)

        # Problem input area - speak or type (radio buttons)
        self.input_mode_var = tk.StringVar(value='type')
        input_mode_frame = tk.Frame(self)
        input_mode_frame.pack(pady=10)
        self.rb_speak = tk.Radiobutton(input_mode_frame, text=self.translations['en']['speak_problem'], variable=self.input_mode_var, value='speak')
        self.rb_speak.grid(row=0, column=0, padx=10)
        self.rb_type = tk.Radiobutton(input_mode_frame, text=self.translations['en']['type_problem'], variable=self.input_mode_var, value='type')
        self.rb_type.grid(row=0, column=1, padx=10)

        self.problem_entry = tk.Text(self, height=4, width=60)
        self.problem_entry.pack(pady=5)

        self.btn_submit = tk.Button(self, text=self.translations['en']['submit'], command=self.submit_problem)
        self.btn_submit.pack(pady=10)

        # Recommendation display
        rec_label_frame = tk.Frame(self)
        rec_label_frame.pack(pady=5, fill='x')
        self.rec_label = tk.Label(rec_label_frame, text=self.translations['en']['recommendation'], font=('Arial', 14, 'bold'))
        self.rec_label.pack(anchor='w')

        self.rec_text = tk.Text(self, height=10, width=80, state='disabled')
        self.rec_text.pack(pady=5)

        # Additional info label and input
        add_info_label_frame = tk.Frame(self)
        add_info_label_frame.pack(pady=5, fill='x')
        self.add_info_label = tk.Label(add_info_label_frame, text=self.translations['en']['additional_info'])
        self.add_info_label.pack(anchor='w')

        self.add_info_entry = tk.Text(self, height=4, width=60)
        self.add_info_entry.pack(pady=5)

        # Initialize language UI texts
        self.change_language('en')

    def change_language(self, lang):
        self.selected_lang = lang
        t = self.translations[lang]
        self.lang_var.set(lang)
        self.btn_choose.config(text=t['choose_image'])
        self.btn_capture.config(text=t['capture_image'])
        self.rb_speak.config(text=t['speak_problem'])
        self.rb_type.config(text=t['type_problem'])
        self.btn_submit.config(text=t['submit'])
        self.rec_label.config(text=t['recommendation'])
        self.add_info_label.config(text=t['additional_info'])

    def choose_image(self):
        file_path = filedialog.askopenfilename(
            title=self.translations[self.selected_lang]['choose_image'],
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.img_path = file_path
            self.display_image(file_path)

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            speak(self.translations[self.selected_lang]['error_camera'], self.selected_lang)
            messagebox.showerror("Error", self.translations[self.selected_lang]['error_camera'])
            return
        speak(self.translations[self.selected_lang]['capturing'], self.selected_lang)
        # Delay for 5 seconds before capturing (blocking)
        self.after(5000, cap.release)
        ret, frame = cap.read()
        if ret:
            img_path = 'captured_crop.jpg'
            cv2.imwrite(img_path, frame)
            self.img_path = img_path
            self.display_image(img_path)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((400, 300), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(img)
        self.img_label.imgtk = imgtk
        self.img_label.config(image=imgtk)

    def submit_problem(self):
        problem_text = self.problem_entry.get("1.0", tk.END).strip()
        if self.input_mode_var.get() == 'speak' and not problem_text:
            try:
                recognized_text = recognize_speech(VOSK_MODEL_PATH)
                if recognized_text:
                    problem_text = recognized_text
            except Exception:
                pass  # Ignore and proceed

        # Make farm input optional: no warning if empty
        if not self.img_path or not os.path.exists(self.img_path):
            messagebox.showwarning("Image Needed", "Please select or capture a crop image first.")
            return

        # Predict disease from image
        self.disease_class = predict_disease(self.img_path, self.model)
        disease_display = self.disease_class.replace('_', ' ')

        # Speak disease diagnosed
        disease_text = {
            'en': f"Identified disease: {disease_display}",
            'hi': f"पहचाना गया रोग: {disease_display}",
            'bn': f"পহচানা রোগ: {disease_display}",
            'pa': f"ਪਛਾਣਿਆ ਗਿਆ ਰੋਗ: {disease_display}",
        }.get(self.selected_lang, f"Identified disease: {disease_display}")

        speak(disease_text, self.selected_lang)

        # Get recommendation
        recommendation = get_recommendation(self.disease_class, self.selected_lang)
        recommendation_lines = [recommendation.get('advice', '')]
        if recommendation.get('pesticides'):
            recommendation_lines.append(
                f"{self.translations[self.selected_lang].get('pesticides', 'Pesticides')}: {', '.join(recommendation['pesticides'])}")
        if recommendation.get('fertilizers'):
            recommendation_lines.append(
                f"{self.translations[self.selected_lang].get('fertilizers', 'Fertilizers')}: {', '.join(recommendation['fertilizers'])}")
        if recommendation.get('dosage'):
            recommendation_lines.append(
                f"{self.translations[self.selected_lang].get('dosage', 'Dosage')}: {recommendation['dosage']}")

        full_recommendation = "\n".join(recommendation_lines)

        # Display recommendation text
        self.rec_text.config(state='normal')
        self.rec_text.delete("1.0", tk.END)
        self.rec_text.insert(tk.END, full_recommendation)
        self.rec_text.config(state='disabled')

        # Speak full recommendation
        speak(f"{self.translations[self.selected_lang].get('recommendation', 'Recommendation')}: {full_recommendation}",
              self.selected_lang)

        # Ask for more tips
        speak(self.translations[self.selected_lang]['need_more_tips'], self.selected_lang)

        # Get yes/no voice or typed response
        response = ''
        if self.selected_lang == 'hi':
            try:
                response = recognize_speech(VOSK_MODEL_PATH, duration=5).lower()
            except Exception:
                response = input("हाँ या नहीं?\n").lower()
        else:
            response = input("Yes or No?\n").lower()

        if response in self.translations[self.selected_lang]['yes']:
            speak(self.translations[self.selected_lang]['pesticide_safety_tips'], self.selected_lang)
            messagebox.showinfo("Safety Tips", self.translations[self.selected_lang]['pesticide_safety_tips'])
        else:
            speak(self.translations[self.selected_lang]['thank_you'], self.selected_lang)


def main():
    app = PlantDiseaseApp()
    app.mainloop()


if __name__ == "__main__":
    main()
