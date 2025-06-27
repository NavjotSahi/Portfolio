#app.py

import streamlit as st
from pathlib import Path
from PIL import Image
import base64
import streamlit.components.v1 as components

#--- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "Resume_Navjot.pdf"
profile_pic_file = current_dir / "profile.jpg"

#--- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Navjot Sahi"
PAGE_ICON = "🤖"
NAME = "Navjot Sahi"
DESCRIPTION = """
Artificial Intelligence enthusiast with a strong foundation in Python, deep learning, and backend development.
Skilled in building intelligent systems. Passionate about applying machine learning and modern AI tools to solve 
real-world problems through scalable solutions.
"""
EMAIL = "sahinavjot0@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": {"url": "https://www.linkedin.com/in/navjot-sahi-360470268/", "icon": "linkedin"},
    "GitHub": {"url": "https://github.com/NavjotSahi", "icon": "github"},
    "Leetcode": {"url": "https://leetcode.com/u/NavjotSahi/", "icon": current_dir / "assets" / "leetcode.png"},
}
PROJECTS = {
    "🏆 AI-Powered Academic Dashboard & RAG Chatbot": {
        "stack": "Django, Streamlit, LangChain, Google Gemini, ChromaDB",
        "description": [
            "Built a personalized academic dashboard with role-based access and real-time grade tracking.",
            "Integrated a course-specific chatbot using LangChain and Google Gemini via a RAG pipeline."
        ],
        "link": "https://github.com/NavjotSahi/CourseCompanionAI"
    },
    "🏆 HealthMate: AI-Powered Health Chatbot": {
        "stack": "Python, TensorFlow, Kubernetes, Vultr Cloud",
        "description": [
            "Engineered an NLP-driven health chatbot, deployed on Vultr Cloud.",
            "<b>Secured Top 5 placement out of 3,500 participants</b> in the Vultr Cloud Hackathon by optimizing NLP algorithms."
        ],
        "link": "https://github.com/NavjotSahi/HealthMate-AI-Powered-Health-Chatbot"
    },
    "🏆 Tomato Disease Detection System": {
        "stack": "Python, Django, ResNet-50, TensorFlow",
        "description": [
            "Built a web-based application using Django for detecting tomato plant diseases.",
            "Trained ResNet-50 on the Tomato Disease Dataset, achieving <b>99% accuracy</b>."
        ],
        # "link": "https://github.com/NavjotSahi/Tomato-Disease-Detection"
    },
    "🏆 Skincare Recommendation System": {
        "stack": "Java, CNN, Collaborative Filtering",
        "description": [
            "Designed a CNN-based recommendation system in Java, leveraging collaborative filtering to personalize skincare recommendations.",
            "Conducted user testing with a dataset of 1,000+ entries, improving recommendation accuracy by 15%."
        ],
        # "link": "https://github.com/NavjotSahi/Skincare-Recommendation-System"
    }
}

#--- SET PAGE CONFIG AS THE FIRST STREAMLIT COMMAND ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")


#--- HELPER FUNCTION TO ENCODE LOCAL IMAGES ---
def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
#--- INJECT ALL CSS ---
CUSTOM_CSS = """
<style>
    /* --- GOOGLE FONT & BASE STYLES --- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
        background: #0f0c29; /* Fallback for older browsers */
        background: -webkit-linear-gradient(to right, #000000, #302b63, #ffffff);
        background: linear-gradient(to right, #000000, #302b63, #ffffff);
        color: #f0f2f5;
    }
    
    /* --- HIDE STREAMLIT ELEMENTS --- */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 2rem; } /* Add more space at the top */

    /* --- ANIMATIONS --- */
    @keyframes slideUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes revealUnderline { from { width: 0; } to { width: 100%; } }

    /* --- HERO SECTION & SOCIAL ICONS --- */
    .stImage img { border-radius: 50%; border: 5px solid #fff; box-shadow: 0 10px 40px rgba(255, 255, 255, 0.2); }
    
        /* Style for the description paragraph inside the hero container */
    .hero-container p {
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }
      
          /* Style for the new particle animation container */
    .particle-container {
        border-radius: 15px; /* Match the other cards */
        overflow: hidden;    /* Important to clip the iframe corners */
        height: 400px;       /* Give it a fixed height */
        border: 1px solid rgba(255, 255, 255, 0.1); /* Match other cards */
    }
    .social-icons-overlay {
        display: flex;
        gap: 15px;
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 25px;
        padding: 8px 15px;
        justify-content: flex-start;
        flex-wrap: wrap;
        max-width: 185px;
        margin-top: 10px;
        margin-bottom: 20px;
        margin-left: 0;
    }

    .stTitle, h1 { font-weight: 700; font-size: 4rem; color: #fff; text-shadow: 0 0 10px rgba(255, 255, 255, 0.5); }
    .social-icons { display: flex; justify-content: flex-start; gap: 15px; margin-top: 1rem; }
    .social-icon { display: inline-block; width: 40px; height: 40px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.1); text-align: center; line-height: 40px; transition: all 0.3s ease; }
    .social-icon:hover { transform: scale(1.2) rotate(10deg); background-color: rgba(255, 255, 255, 0.3); }
    .social-icon img { width: 20px; height: 20px; vertical-align: middle; }
    

    /* --- SECTION HEADERS --- */
    h2 { font-weight: 600; font-size: 2rem; color: #fff; padding-bottom: 10px; margin-top: 3rem; display: inline-block; position: relative; }
    h2::after { content: ''; position: absolute; bottom: 0; left: 0; height: 3px; background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%); animation: revealUnderline 1s ease-out forwards; }

    /* --- CUSTOM DOWNLOAD BUTTON --- */
    div[data-testid="stDownloadButton"] > button { background-image: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%); color: #0f0c29; border-radius: 20px; padding: 10px 20px; border: none; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0, 242, 254, 0.4); }
    div[data-testid="stDownloadButton"] > button:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0, 242, 254, 0.5); }

    /* --- SKILL PILLS --- */
    .skill-pill { display: inline-block; background-color: rgba(255, 255, 255, 0.1); color: #f0f2f5; padding: 8px 18px; margin: 4px; border-radius: 20px; font-weight: 400; transition: all 0.3s ease; border: 1px solid rgba(255, 255, 255, 0.1); }
    .skill-pill:hover { transform: scale(1.1); background-color: rgba(255, 255, 255, 0.2); box-shadow: 0 0 15px rgba(0, 242, 254, 0.5); }
    
    /* --- CARD STYLING & ANIMATIONS --- */
    .project-card { position: relative; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 25px; margin-bottom: 25px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37); background-color: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease; opacity: 0; animation: slideUp 0.8s ease-out forwards; }
    .project-card:hover { transform: translateY(-10px); box-shadow: 0 0 25px rgba(0, 242, 254, 0.5); border-color: rgba(0, 242, 254, 0.5); }
    .project-card:nth-of-type(1) { animation-delay: 0.2s; } .project-card:nth-of-type(2) { animation-delay: 0.4s; } .project-card:nth-of-type(3) { animation-delay: 0.6s; } .project-card:nth-of-type(4) { animation-delay: 0.8s; } .project-card:nth-of-type(5) { animation-delay: 1.0s; } .project-card:nth-of-type(6) { animation-delay: 1.2s; }
    .project-card h3 { color: #fff; margin-top: 0; } .project-card .tech-stack { font-style: italic; color: #a9a9a9; } .project-card ul { padding-left: 20px; margin-bottom: 10px; }
    .project-card a { text-decoration: none; color: #4facfe; font-weight: 600; transition: color 0.3s ease; }
    .project-card a:hover { color: #00f2fe; }

</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


#--- HERO SECTION ---
col1, col2 = st.columns([1, 2.5], gap="large")
with col1:
    if Path(profile_pic_file).is_file():
        profile_pic = Image.open(profile_pic_file)
        st.image(profile_pic, width=280)

with col2:
    # Create nested columns inside the second main column.
    sub_col1, sub_col2 = st.columns([0.6, 0.4], gap="medium")
    
    with sub_col1:
        # This is the text content, wrapped in its glassmorphism container
        st.markdown('<div class="hero-container">', unsafe_allow_html=True)
        st.title(NAME)
        st.write(DESCRIPTION)
        if Path(resume_file).is_file():
            with open(resume_file, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(
                label="📄 Download Resume",
                data=PDFbyte,
                file_name=resume_file.name,
                mime="application/octet-stream",
            )
        st.markdown("📫 [sahinavjot0@gmail.com](mailto:sahinavjot0@gmail.com)")
        st.markdown("📱 [+91-8168137436](tel:+918168137436)")

        st.markdown('</div>', unsafe_allow_html=True)

    with sub_col2:
        # This is your working particle animation, placed in the second column.
        # We wrap it in a div so we can style the container.
        # st.markdown('<div class="particle-container">', unsafe_allow_html=True)
    
        particles_html = """
        <!DOCTYPE html>
        <html>
          <head>
            <style>
              html, body {
                margin: 0;
                padding: 0;
                overflow: hidden;
                /* THE FIX: Make the iframe background transparent */
                background: transparent;
              }
              #particles-js {
                position: absolute;
                width: 100%;
                height: 100%;
              }
            </style>
          </head>
          <body>
            <div id="particles-js"></div>
            <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
            <script>
              particlesJS("particles-js", {
                "particles": { "number": { "value": 120, "density": { "enable": true, "value_area": 800 } }, "color": { "value": "#ffffff" }, "shape": { "type": "circle" }, "opacity": { "value": 0.5 }, "size": { "value": 3, "random": true }, "line_linked": { "enable": true, "distance": 150, "color": "#ffffff", "opacity": 0.4, "width": 1 }, "move": { "enable": true, "speed": 2, "direction": "none", "out_mode": "out" } },
                "interactivity": { "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" } }, "modes": { "grab": { "distance": 140, "line_linked": { "opacity": 1 } }, "push": { "particles_nb": 4 } } },
                "retina_detect": true
              });
            </script>
          </body>
        </html>
        """
        components.html(particles_html, height=400, scrolling=False)
    

# --- SOCIAL LINKS ---
# st.write("#")
st.subheader("Socials")
social_icons_html_parts= []
mime_map = {".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg"}
for platform, info in SOCIAL_MEDIA.items():
        icon_src = ""
        if isinstance(info['icon'], Path):
            ext = info['icon'].suffix.lower()
            mime_type = mime_map.get(ext, "application/octet-stream")
            icon_src = f"data:{mime_type};base64,{load_image_as_base64(info['icon'])}"
        else:
            icon_src = f"https://img.icons8.com/ios-filled/50/ffffff/{info['icon']}.png"
        social_icons_html_parts.append(f'<a href="{info["url"]}" target="_blank" class="social-icon"><img src="{icon_src}" alt="{platform}"></a>')
social_icons_html = f'<div class="social-icons-overlay">{"".join(social_icons_html_parts)}</div>'
st.markdown(social_icons_html, unsafe_allow_html=True)
    
st.markdown('</div>', unsafe_allow_html=True)


#--- WRAPPER FOR ALL ANIMATED SECTIONS ---
st.markdown('<div class="animated-section-wrapper">', unsafe_allow_html=True)

#--- TECHNICAL SKILLS ---
# st.write("#")
st.subheader("Technical Skills")
skills = {
    "Programming": ["Python", "Java", "C", "JavaScript"],
    "Web Development": ["HTML", "CSS", "JavaScript"],
    "Database Management": ["MySQL", "Oracle", "PostgreSQL"],
    "ML & Data Science": ["TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Pandas"],
    "Dev Tools": ["Node.js", "Django", "Streamlit", "LangChain"],
    "AI & Vector Tech": ["ChromaDB", "Google Gemini"]
}
for category, skill_list in skills.items():
    st.markdown(f"<h5 style='margin-top:20px; color:#00f2fe;'>{category}</h5>", unsafe_allow_html=True)
    skill_html = "".join([f'<span class="skill-pill">{skill}</span>' for skill in skill_list])
    st.markdown(f"<div>{skill_html}</div>", unsafe_allow_html=True)

# --- PROJECTS ---
st.write("#")
st.subheader("Projects")
st.write("---")
for project, details in PROJECTS.items():
    description_html = "".join([f"<li>{item}</li>" for item in details["description"]])
    
    # --- THIS IS THE FIX ---
    # Check if a 'link' key exists and is not empty for the project
    if details.get("link"):
        link_html = f"""<a href="{details['link']}" target="_blank">View Code on GitHub</a>"""
    else:
        link_html = ""  # If no link, create an empty string
    
    # Now, build the final card HTML, including the link_html variable
    card_html = f"""
    <div class="project-card">
        <h3>{project}</h3>
        <p class="tech-stack"><b>Tech Stack:</b> {details['stack']}</p>
        <ul>{description_html}</ul>
        {link_html}
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    
#--- INTERNSHIPS ---
st.write("#")
st.subheader("Internships")
st.write("---")
#Display both internship cards
st.markdown("""
    <div class="project-card">
        <h3>💼 Generative AI Intern | SmartBridge (Remote)</h3>
        <p class="tech-stack"><i>June 2025 – Present</i></p>
        <ul>
            <li>Completed 60-hour virtual internship focused on generative AI models (VAE, GAN, BERT, LSTM) and tools like Gemini and FastAPI, gaining hands-on experience in text generation, summarization, and chatbot development.</li>
        </ul>
    </div>
    <div class="project-card">
        <h3>💼 Social Intern | Udit Kunj Foundation (Kaithal, Haryana)</h3>
        <p class="tech-stack"><i>June 2023</i></p>
        <ul>
            <li>Spearheaded outreach initiatives for gender equality, anti-drug awareness, and environmental programs, engaging with 500+ participants and achieving a 25% increase in program enrollment.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # --- CLOSE THE WRAPPER DIV ---