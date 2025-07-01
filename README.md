🌿 EcoVerse
EcoVerse is a voice-assisted environmental tool designed to help users become more climate-conscious through two impactful features:

🔍 Eco Tip Generator — Personalized climate tips based on your city, issues, transport habits, and electricity usage.

🎙 Carbon Confessor — A witty “offline carbon therapist” that listens to your eco-sins and delivers guilt-tripping yet encouraging feedback.

-----

🛠 Tech Stack
Frontend: HTML, CSS, JavaScript (Voice Input via Web Speech API)
Backend: Python, Flask
Libraries: Flask, speech_recognition, pyttsx3, jinja2

----

🌟 Features
✅ Eco Tip Generator
-Inputs: City, Climate Issue, Transport Mode, Electricity Usage
-Output: Custom sustainability tip
-Supports voice input for all fields
-Designed to be inclusive for both rural and urban users

🎤 Carbon Confessor
-Inputs: Free-text or voice confession of carbon-heavy habits
-Output: Sarcastic, witty, guilt-tripping feedback
-Optional offline text-to-speech (TTS) using pyttsx3

-------


📁 Project Structure

EcoVerse/
│
├── static/
│   ├── style.css
│   ├── voiceInput.js
│   ├── background.jpg
│   └── background.mp4
│
├── templates/
│   ├── index.html               # Tip input form
│   ├── tip.html                 # Tip output page
│   └── carbon_confessor.html    # Confession input + feedback
│
├── main.py                     # Core Flask application
├── tips_generator.py           # Logic for eco tip generation
├── feedback_generator.py       # Rule-based witty feedback engine
├── voicetip.py                 # (Optional) TTS for confessions
└── README.md

---------

🚀 Getting Started
1. Install dependencies
   pip install flask pyttsx3 speechrecognition

2. Run the app
   python main.py

3. Open in browser
   http://127.0.0.1:5000

--------

## 👥 Team & Contributions

**Kiyara Chandrawat** — Frontend Design (HTML/CSS), UI Styling, Voice Input Integration  
**Janhvi** — Backend Logic (Flask), Carbon Confessor Engine, Text-to-Speech Integration

🤝 We collaborated closely to ensure a smooth, feature-rich, and intuitive experience.

---

## 🧭 Future Enhancements

- 📸 OCR-based Utility Bill Scanning for automated energy analysis  
- 🌐 Support for Regional Languages (beyond English/Hindi)  
- 🕹️ Gamified Carbon Tracker with scoreboards and tips  
- 🎧 Offline Voice Input using Vosk API

-----


💬 Philosophy
EcoVerse isn’t just a tool—it’s your personal, offline carbon conscience.
Smart, sassy, and sustainable. 🌏

