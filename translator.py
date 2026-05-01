# import various libraries/modules that are used in this code
import customtkinter as ctk
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
import pyttsx3
from indic_transliteration.sanscript import transliterate, DEVANAGARI, ITRANS 
from gtts import gTTS
from playsound import playsound
import os
import threading

# Global variable that store translated text
translated_text = ""

# create translator object and engine for translating text to speech
translator = Translator()
engine = pyttsx3.init() 

# empty list created to store translation history
history = []

# Set appearance of customtkinter window to Light mode.
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry('760x550')
app.title("Language Translator")

# Lanuage Mapping
lang_dict = {v: k for k, v in LANGUAGES.items()}


def translate():  # Function that translates entered text into another language.
    try:
        # Gets entered text from input box
        text = input_box.get("1.0", "end").strip()
        dest_lang = lang_dict[dest_combo.get()]

        if text == "":
            output_box.delete(1.0, "end")
            output_box.insert(1.0, "Enter text!")
            return

        # Translate entered text using googletrans library
        result = translator.translate(text, dest=dest_lang)

        # Store translated text globally
        global translated_text
        translated_text = result.text

        # Gets the pronunciation for the word or phrase if there is any.
        pronunciation = result.pronunciation

        # If no pronunciation was returned, set it to "Not available."
        if pronunciation is None:
            pronunciation = "Not available."

        # Display translated text along with its pronunciation on screen in Output Box.
        output_box.delete(1.0, "end")
        output_box.insert(1.0, f"🌐 Translated ({dest_combo.get()}): \n{result.text}\n\n "
                              f"🔤 Pronunciation (English): \n{pronunciation}")

        # Update Detected Language Label
        detected_label.configure(text=f"Detected: {result.src}")

        # Append to History List
        history.append(f"{text} → {result.text}")

        # Call function to update History Box display.
        update_history()

    except Exception as e:
        print(e)
        output_box.delete(1.0, "end")
        output_box.insert(1.0, "Error!")


def speak_output():  # Function to get speak output
    try:
        # Check to make sure some text has been selected
        if translated_text == "":
            return

        # Convert destination language code
        lang_code = lang_dict[dest_combo.get()]

        # Use Google TTS
        tts = gTTS(text=translated_text, lang=lang_code)

        # Save and play generated TTS file
        tts.save("voice.mp3")
        playsound("voice.mp3")

        # Remove TTS file
        os.remove("voice.mp3")

    except Exception as e:
        print(e)


def voice_input():      # Function to collect voice input
    # Start listening for user's voice input in separate thread.
    threading.Thread(target=listen_voice).start()

def listen_voice():     # Function to listen user's voice
    try:
        # Create SR recognizer object.
        r = sr.Recognizer()

        # Update Detected Language Label while waiting for user to finish speaking. 
        detected_label.configure(text="Listening...")

        # Open default microphone device and start recording for up to 5 seconds.
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        # Attempt to transcribe recorded audio into text.
        text = r.recognize_google(audio)

        # Clear Input Box and insert recognized voice input into Input Box. 
        input_box.delete(1.0, "end")
        input_box.insert(1.0, text)

        # Update Detected Language Label once transcription is complete. 
        detected_label.configure(text="Voice captured")

    except sr.WaitTimeoutError:
        detected_label.configure(text="No speech detected")
    except sr.UnknownValueError:
        detected_label.configure(text="Could not understand")
    except sr.RequestError:
        detected_label.configure(text="Internet error")
    except Exception as e:
        print(e)
        detected_label.configure(text="Voice error")


def copy_text():    # Function that copies text
    app.clipboard_clear()
    app.clipboard_append(output_box.get(1.0, "end"))

def clear():        # Function that clears text
    input_box.delete(1.0, "end")
    output_box.delete(1.0, "end")
    history_box.delete(1.0, "end")

def update_history():   # Function that update history and show over last 5 translations
    history_box.delete(1.0, "end")
    for item in history[-5:]:
        history_box.insert(1.0, item + "\n")

# --- UI Setup ---

# Title="Language Translator"
title = ctk.CTkLabel(app, text="Language Translator", font=("Arial", 22, "bold"))
title.pack(pady=10)

# input box= text you want to get translation for
input_box = ctk.CTkTextbox(app, height=100, width=600)
input_box.pack(pady=10)

# combobox=stores various languages as drop-down list
dest_combo = ctk.CTkComboBox(app, values=list(lang_dict.keys()))
dest_combo.set("hindi")
dest_combo.pack(pady=5)

detected_label = ctk.CTkLabel(app, text="Detected: -")
detected_label.pack()

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

# Ensure these command functions (translate, voice_input, speak_output) exist
ctk.CTkButton(btn_frame, text="Translate", command=translate).grid(row=0, column=0, padx=5)
ctk.CTkButton(btn_frame, text="🎤 Speak", command=voice_input).grid(row=0, column=1, padx=5)
ctk.CTkButton(btn_frame, text="🔊 Listen", command=speak_output).grid(row=0, column=2, padx=5)
ctk.CTkButton(btn_frame, text="📋 Copy", command=copy_text).grid(row=0, column=3, padx=5)
ctk.CTkButton(btn_frame, text="🗑️ Clear", command=clear).grid(row=0, column=4, padx=5)

# output box= displays the translated text
output_box = ctk.CTkTextbox(app, height=100, width=600)
output_box.pack(pady=10)

history_label = ctk.CTkLabel(app, text="History")
history_label.pack()

# history box= display history of over last 5 translations
history_box = ctk.CTkTextbox(app, height=100, width=600)
history_box.pack(pady=5)

app.mainloop()
