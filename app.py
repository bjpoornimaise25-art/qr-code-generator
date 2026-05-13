import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("🔳 QR Code Generator")

text = st.text_input("Enter text or URL")

if st.button("Generate QR Code"):

    if text.strip() == "":
        st.warning("Please enter some text or URL.")
    else:
        # Generate QR
        qr = qrcode.make(text)

        # Display QR
        st.image(qr, caption="Generated QR Code", use_container_width=False)

        # Save image to bytes
        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        # Download button
        st.download_button(
            label="📥 Download QR Code",
            data=buffer.getvalue(),
            file_name="qrcode.png",
            mime="image/png"
        )
