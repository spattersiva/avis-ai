import streamlit as st
from model import generate_image
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AVIS AI",
    page_icon="♾️",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1e1f26, #14151a);
    font-family: 'Poppins', sans-serif;
}

/* ---------- TITLE ---------- */
.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
    margin-bottom: 20px;
    text-shadow: 0px 4px 12px rgba(0,0,0,0.5);
}

/* ---------- MAIN CARD ---------- */
.card {
    background: rgba(255, 255, 255, 0.07);
    border-radius: 24px;
    padding: 30px;
    max-width: 700px;
    margin: auto;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 10px 35px rgba(0,0,0,0.45);
    animation: fadeIn 1.1s ease-in-out;
}

/* ---------- IPHONE STYLE INPUT BOX ---------- */
.prompt-box textarea {
    border-radius: 22px !important;
    padding: 18px !important;
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    backdrop-filter: blur(18px);
    color: #fff !important;
    font-size: 16px !important;
    box-shadow: inset 0px 0px 12px rgba(255,255,255,0.05),
                0px 8px 25px rgba(0,0,0,0.3);
}

/* ---------- GENERATE BUTTON ---------- */
.generate-btn {
    width: 100%;
    padding: 14px 0;
    border-radius: 14px;
    border: none;
    font-size: 20px;
    font-weight: 600;
    color: white;
    background: linear-gradient(90deg, #4b74ff, #6d4bff, #a14bff);
    background-size: 300%;
    transition: 0.4s ease;
}

.generate-btn:hover {
    background-position: right;
    transform: scale(1.05);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
}

/* ---------- PERFECT SQUARE OUTPUT BOX ---------- */
.output-container {
    width: 450px;
    height: 450px;
    margin: 30px auto;
    padding: 14px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 10px 35px rgba(0,0,0,0.45);
    backdrop-filter: blur(16px);
    display: flex;
    align-items: center;
    justify-content: center;
}

.output-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 18px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
}

/* ---------- ANIMATIONS ---------- */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("<h1 class='main-title'> AVIS AI ♾️ </h1>", unsafe_allow_html=True)


# ---------- UI CARD ----------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # ----- INPUT BOX -----
    st.markdown("<div class='prompt-box'>", unsafe_allow_html=True)
    prompt = st.text_area(
        "Enter your prompt",
        height=140,
        placeholder="e.g., A futuristic cyberpunk city floating above the ocean at sunset 🌇"
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # ----- GENERATE BUTTON -----
    clicked = st.button("✨ Generate Image", key="gen_button")

    if clicked:
        if not prompt.strip():
            st.warning("⚠️ Please enter a prompt first.")
        else:
            with st.spinner("🎨 Creating your AI masterpiece... Hold on!"):
                img_path = generate_image(prompt)

            st.success("🔥 Image generated successfully!")

            # ----- OUTPUT IMAGE IN SQUARE BOX -----
            st.markdown("<div class='output-container'>", unsafe_allow_html=True)
            st.image(img_path, use_container_width=False, output_format="PNG")
            st.markdown("</div>", unsafe_allow_html=True)

            # ----- DOWNLOAD BUTTON -----
            with open(img_path, "rb") as f:
                img_bytes = f.read()

            st.download_button(
                label="📥 Download Image",
                data=img_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )

    st.markdown("</div>", unsafe_allow_html=True)
