Language Translator App

It is a modern Python-based GUI application that translates text between multiple languages with voice input and text-to-speech output support.


 Features:

-  Multi-language Translation using Google Translate API
-  Voice Input (Speech Recognition)
-  Text-to-Speech Output
-  Automatic Language Detection
-  Translation History (last 5 entries)
-  Copy to Clipboard Functionality
-  Clear Input/Output Option
-  Simple and user-friendly GUI built with CustomTkinter



 Tech Stack:

- Python
- CustomTkinter (GUI)
- googletrans
- SpeechRecognition
- pyttsx3
- gTTS (Google Text-to-Speech)
- playsound
- indic-transliteration



 Project Structure:

language-translator-app/
│── translator.py
│── requirements.txt
│── README.md



 Installation & Setup:

1️- Clone the Repository

git clone https://github.com/your-username/language-translator-app.git
cd language-translator-app

2️- Install Dependencies

pip install -r requirements.txt

3️- Run the Application

python translator.py



 How It Works:

1. Enter text in the input box OR use 🎤 voice input
2. Select the target language from dropdown
3. Click Translate
4. View translated text along with pronunciation
5. Use 🔊 to listen to translation
6. Access last 5 translations in history



Screenshots:
<img width="945" height="721" alt="Screenshot 2026-05-02 001141" src="https://github.com/user-attachments/assets/ef2cd761-ed53-417e-af99-a157f18461cc" />
<img width="947" height="721" alt="image" src="https://github.com/user-attachments/assets/d6f1f2ab-5ed1-4652-b129-ad9e7bb4af51" />



Notes:

- Internet connection is required for translation and speech recognition
- Ensure microphone access is enabled for voice input
- Install PyAudio manually if voice input doesn’t work



Requirements:

customtkinter
googletrans==4.0.0-rc1
SpeechRecognition
pyttsx3
indic-transliteration
gTTS
playsound
pyaudio



Team Spartan
  Members:
     - Medhavi Bisht (Leader)
     - Devyanshi Sah
     - Sneha Pal

License:
This project is open-source and free to use.
