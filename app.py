import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io

st.set_page_config(page_title="AI Detector", page_icon="🤖")

st.title("🤖 AI Image Detector")
st.write("Upload a photo to check if it might be AI-generated.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

def simple_ai_check(image: Image.Image):
    img = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    if laplacian_var < 50:
        return "⚠️ Possibly AI-generated (very smooth / low noise)"
    else:
        return "✅ Likely camera-captured"

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    verdict = simple_ai_check(image)
    st.subheader("Result")
    st.write(verdict)
