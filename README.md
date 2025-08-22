# 🤖 AI Image Detector

A simple web app that lets you upload a photo and check whether it might be **AI-generated** or **camera-captured**.
Built with [Streamlit](https://streamlit.io/).

## 🚀 Live Demo
Once deployed, your app will be available at:
https://your-username-ai-detector.streamlit.app

## 📂 Features
- Upload `.jpg`, `.jpeg`, or `.png` images
- Instant analysis based on **image smoothness and noise patterns**
- Returns a result:
  - ✅ Likely camera-captured
  - ⚠️ Possibly AI-generated

## 🛠 How It Works
The app uses a simple image quality check:
- Real photos usually have **natural noise and texture**
- AI-generated images often look **too smooth**
- A variance calculation on edges helps estimate this difference

> ⚠️ Note: This is a **basic demo** — not 100% accurate.

## 📦 Installation (for developers)
Clone this repo and install dependencies:
```
git clone https://github.com/your-username/ai-detector.git
cd ai-detector
pip install -r requirements.txt
streamlit run app.py
```

## 🌍 Deployment
This project is built for easy deployment with **Streamlit Cloud**:
1. Upload files to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo and select `app.py`
4. Deploy 🚀
