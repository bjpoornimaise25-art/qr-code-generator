import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("🔳 QR Code Generator")

text = st.text_input("Enter text or URL")

if st.button("Generate QR Code"):

    if text.strip() == "":
        st.warning("Please enter some text or URL.")

    else:
        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save image into memory
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Display image
        st.image(buffer.getvalue(), caption="Generated QR Code")

        # Download button
        st.download_button(
            label="📥 Download QR Code",
            data=buffer.getvalue(),
            file_name="qrcode.png",
            mime="image/png"
        )
