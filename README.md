# 🎙️ Jarvis – Python Voice Assistant

Jarvis is a voice-controlled desktop assistant built with Python. Say the wake word **"Jarvis"**, give a command, and it will open websites, play your favourite songs, read out the latest news, or answer general questions using a **local AI model (Llama 3.2 via Ollama)** – no paid AI API needed.

---

## ✨ Features

- 🗣️ **Wake word detection** – listens for "Jarvis" before taking a command
- 🌐 **Open websites** – Google, Facebook, YouTube, LinkedIn by voice
- 🎵 **Play songs** – plays songs from your own `musicLibrary.py`
- 📰 **Live news** – reads the top 5 Indian headlines using the NewsData.io API
- 🤖 **AI answers** – any other question is answered by Llama 3.2 (3B) running locally through Ollama
- 🔊 **Text-to-speech** – Jarvis talks back using `pyttsx3`

---

## 🛠️ Tech Stack

| Purpose | Library / Tool |
|---|---|
| Language | Python 3 |
| Speech to text | `SpeechRecognition` (Google Web Speech API) |
| Text to speech | `pyttsx3` (SAPI5 voice engine) |
| AI model | `ollama` + `llama3.2:3b` |
| News | `requests` + [NewsData.io](https://newsdata.io) API |
| Browser control | `webbrowser` (built-in) |
| Microphone input | `PyAudio` |

---

## 📁 Project Structure

```
jarvis/
├── main.py            # Main program: wake word, commands, speech
├── client.py          # Small test script for the Ollama AI model
├── musicLibrary.py    # Dictionary of song names -> YouTube links
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/harshguptaa21/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install the Python libraries

```bash
pip install SpeechRecognition pyttsx3 requests ollama pyaudio
```

> If `pyaudio` fails to install on Windows, try `pip install pipwin` then `pipwin install pyaudio`.

### 3. Install Ollama and download the model

1. Download and install Ollama from [ollama.com](https://ollama.com)
2. Pull the model used in this project:

```bash
ollama pull llama3.2:3b
```

### 4. Add your NewsData.io API key

Get a free key from [newsdata.io](https://newsdata.io), then set it as an environment variable instead of writing it in the code:

**Windows (PowerShell)**
```powershell
setx NEWS_API_KEY "your_api_key_here"
```

In `main.py`, replace the hard-coded key with:

```python
import os
newsapi = os.getenv("NEWS_API_KEY")
```

> ⚠️ Never upload your real API key to GitHub.

---

## ▶️ How to Run

```bash
python main.py
```

1. Jarvis says *"Initializing Jarvis...."*
2. Say **"Jarvis"** (wake word)
3. When Jarvis replies *"How can I help you"*, speak your command

---

## 💬 Example Commands

| You say | Jarvis does |
|---|---|
| "Open Google" | Opens google.com |
| "Open YouTube" | Opens youtube.com |
| "Open Facebook" | Opens facebook.com |
| "Open LinkedIn" | Opens linkedin.com |
| "Play tare" | Plays the song saved as `tare` |
| "Tell me the news" | Reads the top 5 headlines from India |
| "What is coding?" | Answers using the local Llama 3.2 model |

### Adding your own songs

Open `musicLibrary.py` and add a new entry:

```python
music = {
    "tare": "https://www.youtube.com/watch?v=...",
    "yoursong": "https://www.youtube.com/watch?v=..."
}
```

Then say **"Play yoursong"**.

---

## 🧠 How It Works

```
Microphone → Wake word "Jarvis"? → Listen to command → processCommand()
                                                          │
        ┌───────────────┬──────────────┬──────────────────┤
        ▼               ▼              ▼                  ▼
   Open website     Play song       Get news      Ask Ollama (Llama 3.2)
                                                          │
                                                          ▼
                                                 Speak answer (pyttsx3)
```

---

## ⚠️ Known Limitations

- Speech recognition needs an **internet connection** (Google Web Speech API)
- The text-to-speech engine uses `sapi5`, so it works on **Windows** only
- Song names must be a single word (e.g. `play tare`)
- Responses from the 3B model can be slower on low-end computers

---

## 🚀 Future Improvements

- Support multi-word song names
- Add more commands (weather, time, reminders, open apps)
- Offline speech recognition
- Cross-platform voice support (Linux/macOS)
- Conversation memory for follow-up questions

---

## 👨‍💻 Author

**Harsh Gupta**
- GitHub: [@harshguptaa21](https://github.com/harshguptaa21)
- LinkedIn: [Harsh Gupta](https://linkedin.com/in/harsh-gupta-05004533a)

---

⭐ If you like this project, give it a star on GitHub!
