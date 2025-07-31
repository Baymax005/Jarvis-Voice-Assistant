import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os
import webbrowser
import pyautogui

recognizer = sr.Recognizer()

# Music dictionary
music = {
    "stealth": "https://www.youtube.com/watch?v=U47Tr9BB_wE",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI",
    "sky fall": "https://www.youtube.com/watch?v=DeumyOzKqgI",  # support both spellings
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
}

def speak(text):
    print("Jarvis says:", text)
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.2)

    pygame.mixer.quit()
    os.remove(filename)

def processCommand(command):
    command = command.lower()
    print("Raw command:", command)

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open stack overflow" in command:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open chat gpt" in command or "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    
    elif "pause video" in command or "play video" in command:
        speak("Toggling video")
        pyautogui.press('space')  # Simulates pressing spacebar

    elif "play" in command:
        for song in music:
            if song.replace(" ", "") in command.replace(" ", ""):
                speak(f"Playing {song}")
                webbrowser.open(music[song])
                return
        speak("I don't know that song.")

    else:
        speak("I didn't understand that.")


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Say 'Jarvis' to activate me.")

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                word = recognizer.recognize_google(audio).lower()
                print("You said:", word)

                if "jarvis" in word:
                    speak("Yes?")
                    time.sleep(0.5)

                    with sr.Microphone() as source2:
                        print("Listening for your command...")
                        audio2 = recognizer.listen(source2, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio2).lower()
                        processCommand(command)

            except sr.WaitTimeoutError:
                print("Timed out.")
            except sr.UnknownValueError:
                print("Speech not clear.")
            except Exception as e:
                print("Error:", e)
