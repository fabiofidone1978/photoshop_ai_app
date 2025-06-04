# Photoshop AI App

Un'app Android sviluppata in Python con Kivy che unisce strumenti di editing immagini e generazione grafica via AI.

---

## ✨ Funzionalità principali

- ✏️ **Modifica immagini locale** (resize, filtri, effetti)
- 🧠 **Generazione immagini AI da prompt** (stile Sora o Midjourney)
- 📱 Interfaccia mobile responsive con Kivy
- 📦 Build automatica APK con GitHub Actions

---

## 🚀 Come usarla

1. Clona il repository:
   ```bash
   git clone https://github.com/fabiofidone1978/photoshop_ai_app.git
   cd photoshop_ai_app
   
   pip install -r requirements.txt
   
   # Avviare l'app
   python main.py
   ```

2. Per generare l'eseguibile Windows (EXE) è possibile usare PyInstaller:
   ```bash
   pip install pyinstaller
   ./build_exe.sh
   ```
   Il file verrà creato nella cartella `dist/` con nome `PhotoshopAI.exe`.
