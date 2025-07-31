
# Jarvis Voice Assistant 🎙️🤖

A Python-based voice assistant named **Jarvis** that listens for a wake word and executes spoken commands using speech recognition and text-to-speech.

## 🚀 Features

- 🔊 Voice activation using the word **"Jarvis"**
- 🌐 Open websites like Google, YouTube, LinkedIn, GitHub, Stack Overflow, ChatGPT
- 🎵 Play specific songs on YouTube by voice
- ⏯️ Pause/play videos via voice using keyboard simulation
- 🎙️ Converts text to speech using gTTS
- 🎧 Plays audio using pygame
- 🖱️ Simulates keypresses using pyautogui

## 📦 Libraries Used

All of these can be installed via `pip`:

| Library              | Description |
|----------------------|-------------|
| `speech_recognition` | Converts speech to text using Google Web Speech API |
| `gTTS`               | Converts text to speech (Google Text-to-Speech) |
| `pygame`             | Plays the generated audio |
| `pyautogui`          | Simulates keyboard input (like spacebar for media control) |
| `webbrowser`         | Opens URLs in your default browser |
| `os` and `time`      | Used for file handling and timing |
| `pyaudio` (required backend) | Microphone input for `speech_recognition` |

### ✅ Installation

Use the following command to install all dependencies:

```bash
pip install SpeechRecognition gTTS pygame pyautogui pyaudio
