
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

## 📥 Installation

### Prerequisites

- Python 3.7 or higher
- A working microphone
- Internet connection (for speech recognition and text-to-speech)

### Install Dependencies

Use the following command to install all required dependencies:

```bash
pip install SpeechRecognition gTTS pygame pyautogui pyaudio
```

**Note for macOS/Linux users:** You may need to install `portaudio` first:
- **macOS:** `brew install portaudio`
- **Ubuntu/Debian:** `sudo apt-get install portaudio19-dev python3-pyaudio`

## 🎮 Usage

1. Clone this repository:
```bash
git clone https://github.com/Baymax005/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
```

2. Install the dependencies (see Installation section above)

3. Run the voice assistant:
```bash
python main.py
```

4. Wait for Jarvis to initialize, then say **"Jarvis"** to activate the assistant

5. After hearing "Yes?", speak your command

## 🗣️ Example Commands

Once Jarvis is activated, you can say:

- **"Open Google"** - Opens Google in your browser
- **"Open YouTube"** - Opens YouTube
- **"Open GitHub"** - Opens GitHub
- **"Open Stack Overflow"** - Opens Stack Overflow
- **"Open LinkedIn"** - Opens LinkedIn
- **"Open ChatGPT"** - Opens ChatGPT
- **"Play Stealth"** - Plays the song "Stealth" on YouTube
- **"Play Skyfall"** - Plays the song "Skyfall" on YouTube
- **"Play Faded"** - Plays the song "Faded" on YouTube
- **"Pause video"** or **"Play video"** - Toggles video playback (simulates spacebar)

## 🛠️ How It Works

1. **Wake Word Detection**: The program continuously listens for the wake word "Jarvis"
2. **Command Recognition**: Once activated, it listens for your command
3. **Command Processing**: The command is processed and appropriate action is taken
4. **Text-to-Speech Feedback**: Jarvis responds with audio confirmation

## 🐛 Troubleshooting

### Microphone not working
- Make sure your microphone is properly connected and set as the default input device
- Check your system's microphone permissions for Python

### PyAudio installation issues
- On **Windows**: Install via `pip install pyaudio`
- On **macOS**: Install portaudio first: `brew install portaudio`, then `pip install pyaudio`
- On **Linux**: Install dependencies: `sudo apt-get install portaudio19-dev python3-pyaudio`

### Speech recognition errors
- Ensure you have a stable internet connection (Google Web Speech API requires internet)
- Speak clearly and at a moderate pace
- Reduce background noise for better recognition

### Audio playback issues
- Make sure your speakers/headphones are working
- Check system volume settings
- Ensure no other application is blocking audio output

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Muhammad Ali** - [Baymax005](https://github.com/Baymax005)

## 🙏 Acknowledgments

- Google Web Speech API for speech recognition
- Google Text-to-Speech (gTTS) for voice synthesis
- The Python community for amazing libraries

---

**Note**: This is a basic voice assistant project. For production use, consider adding error handling, logging, and more robust command parsing
