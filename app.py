
import streamlit as st
from pypdf import PdfReader


st.set_page_config(
    page_title="ResumeAI | AI Resume Analyzer",
    page_icon="✨",
    layout="wide"
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #25204e 0%, transparent 38%),
        radial-gradient(ellipse at 95% 20%, #142e50 0%, transparent 35%),
        #0b1020;
    font-family: 'Inter', sans-serif;
    color: #f8fafc;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: #101629;
    border-right: 1px solid #29334b;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

h1, h2, h3 {
    color: #f8fafc !important;
    letter-spacing: -0.5px;
}

p, label {
    color: #bdc8dc;
}

hr {
    border-color: #29334b !important;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    padding: 12px 4px 22px;
    border-bottom: 1px solid #29334b;
    margin-bottom: 25px;
}

.logo {
    font-size: 26px;
    font-weight: 800;
    color: white;
}

.logo span {
    color: #a78bfa;
}

.nav-tag {
    color: #c4b5fd;
    background: #1b2140;
    border: 1px solid #383564;
    border-radius: 30px;
    padding: 9px 14px;
    font-size: 12px;
}

.hero {
    text-align: center;
    padding: 60px 20px 50px;
    border: 1px solid #343052;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        rgba(124,58,237,0.18),
        rgba(59,130,246,0.08),
        rgba(255,255,255,0.02)
    );
    margin: 25px 0;
}

.eyebrow {
    display: inline-block;
    color: #c4b5fd;
    background: rgba(139,92,246,0.12);
    border: 1px solid #51417d;
    border-radius: 30px;
    padding: 9px 16px;
    font-size: 12px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: clamp(35px, 5vw, 62px);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -2px;
    color: white;
    margin-bottom: 20px;
}

.gradient-text {
    background: linear-gradient(
        90deg, #c4b5fd, #818cf8, #67e8f9
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    max-width: 650px;
    margin: auto;
    color: #b6c2d8;
    font-size: 16px;
    line-height: 1.8;
}

.section-heading {
    text-align: center;
    font-size: 27px;
    font-weight: 700;
    color: white;
    margin-top: 40px;
    margin-bottom: 10px;
}

.section-description {
    text-align: center;
    color: #aab7cf;
    margin-bottom: 30px;
}

.feature-card {
    min-height: 175px;
    height: 100%;
    padding: 23px;
    border-radius: 18px;
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.025)
    );
    border: 1px solid #303a53;
    transition: all 0.25s ease;
}

.feature-card:hover {
    border-color: #8b5cf6;
    transform: translateY(-4px);
    background: rgba(124,58,237,0.12);
}

.feature-icon {
    font-size: 29px;
    margin-bottom: 15px;
}

.feature-card h3 {
    color: white;
    font-size: 18px;
    margin-bottom: 10px;
}

.feature-card p {
    color: #aab7cf;
    font-size: 13px;
    line-height: 1.8;
}

.info-card {
    padding: 20px;
    border-radius: 15px;
    background: #131c31;
    border: 1px solid #2e3b57;
    min-height: 125px;
}

.info-card h3 {
    font-size: 17px;
    color: white;
}

.info-card p {
    color: #aab7cf;
    font-size: 13px;
    line-height: 1.7;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #7c3aed, #6366f1);
    color: white !important;
    border: 1px solid #7770dc;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 600;
    min-height: 48px;
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: #c4b5fd;
    box-shadow: 0 0 22px rgba(124,58,237,0.3);
    color: white;
}

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.035);
    border: 1px dashed #6759a5;
    border-radius: 14px;
    padding: 14px;
}

[data-testid="stTextArea"] textarea {
    background: #111a2d;
    color: white;
    border: 1px solid #36435f;
    border-radius: 12px;
}

[data-testid="stMetric"] {
    background: #131c31;
    border: 1px solid #303b55;
    border-radius: 14px;
    padding: 17px;
}

[data-testid="stMetricLabel"] {
    color: #b5c1d7;
}

[data-testid="stMetricValue"] {
    color: #c4b5fd;
}

.stProgress > div > div {
    background: linear-gradient(90deg, #8b5cf6, #60a5fa);
}

.footer {
    text-align: center;
    color: #75839d;
    border-top: 1px solid #29334b;
    margin-top: 55px;
    padding-top: 25px;
    font-size: 12px;
}

@media (max-width: 700px) {
    .hero {
        padding: 35px 15px;
    }

    .hero-title {
        letter-spacing: -1px;
    }

    .navbar {
        flex-wrap: wrap;
    }
}
</style>
""", unsafe_allow_html=True)



st.sidebar.markdown(
    "<div style='font-size:27px;font-weight:800;'>"
    "✦ Resume<span style='color:#a78bfa;'>AI</span></div>",
    unsafe_allow_html=True
)

st.sidebar.caption("YOUR CAREER ASSISTANT")
st.sidebar.divider()

if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Dashboard"

page = st.sidebar.radio(
    "NAVIGATION",
    ["Dashboard", "Resume Analyzer", "About"],
    key="selected_page"
)

st.sidebar.divider()
st.sidebar.caption("✨ Your career. Your next chapter.")



st.markdown("""
<div class="navbar">
    <div class="logo">✦ Resume<span>AI</span></div>
    <div class="nav-tag">AI-POWERED CAREER TOOLKIT</div>
</div>
""", unsafe_allow_html=True)



if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">
            ✦ &nbsp; YOUR AI-POWERED CAREER TOOLKIT
        </div>

        <div class="hero-title">
            Your next opportunity<br>
            <span class="gradient-text">
                starts with your resume.
            </span>
        </div>

        <div class="hero-description">
            Make your resume stronger with useful feedback.
            Discover matching skills, identify improvement areas,
            and take the next step towards your dream job.
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 1.5, 1])

    with center:
        if st.button(
            "✨ Analyze My Resume",
            use_container_width=True
        ):
            st.session_state["selected_page"] = "Resume Analyzer"
            st.rerun()

    st.markdown("""
    <div class="section-heading">
        Everything you need to stand out
    </div>

    <div class="section-description">
        Simple tools to help you prepare for your next opportunity.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Resume Score</h3>
            <p>
                Understand how well your resume matches
                the skills in your target job description.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✦</div>
            <h3>Smart Feedback</h3>
            <p>
                Identify your relevant strengths and areas
                where your resume could improve.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>Career Ready</h3>
            <p>
                Discover matching skills, skills to learn,
                and job roles related to your resume.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-heading">Your journey starts here</div>

    <div class="section-description">
        Three simple steps to get useful insights from your resume.
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="info-card">
            <h3>📄 01. Upload</h3>
            <p>Upload your resume in PDF format.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="info-card">
            <h3>💼 02. Compare</h3>
            <p>Enter the job description you are interested in.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="info-card">
            <h3>🚀 03. Improve</h3>
            <p>Review your results and download your report.</p>
        </div>
        """, unsafe_allow_html=True)


elif page == "Resume Analyzer":

    st.title("📄 Resume Analyzer")
    st.write(
        "Upload your resume, enter a job description, "
        "and discover your matching skills."
    )

    st.divider()

    resume = st.file_uploader(
        "📎 Upload your resume",
        type=["pdf"]
    )

    job = st.text_area(
        "💼 Enter job description",
        placeholder="Paste the job description here...",
        height=180
    )

    if st.button("✨ Analyze Resume", use_container_width=True):

        if resume and job.strip():

            try:
                reader = PdfReader(resume)
                resume_text = ""

                for pdf_page in reader.pages:
                    resume_text += pdf_page.extract_text() or ""

            except Exception as e:
                st.error(f"Could not read this PDF: {e}")
                st.stop()

            skills = [
                "Python", "Java", "HTML", "CSS",
                "JavaScript", "SQL", "GitHub"
            ]

            found = []
            missing = []

            for skill in skills:
                if (
                    skill.lower() in resume_text.lower()
                    and skill.lower() in job.lower()
                ):
                    found.append(skill)
                elif skill.lower() in job.lower():
                    missing.append(skill)

            st.success("Resume uploaded and analyzed successfully!")

            st.header("📊 Resume Analysis Report")

            total_skills = len(found) + len(missing)
            match = (
                len(found) / total_skills * 100
                if total_skills > 0 else 0
            )

            m1, m2, m3 = st.columns(3)

            with m1:
                st.metric("Matching Skills", len(found))

            with m2:
                st.metric("Skills to Learn", len(missing))

            with m3:
                st.metric(
                    "Resume Match",
                    f"{match:.0f}%" if total_skills > 0 else "N/A"
                )

            if total_skills > 0:
                st.progress(int(match))
                st.write(
                    f"Your resume matches {match:.0f}% "
                    "of the identified required skills."
                )
            else:
                st.info(
                    "No supported skills were identified in the job "
                    "description. Try entering more job requirements."
                )

            st.divider()

            st.subheader("✅ Matching Skills")
            st.write(", ".join(found) if found else "No matching skills identified yet.")

            st.subheader("📚 Skills to Learn")
            st.write(", ".join(missing) if missing else "No missing skills identified.")

            st.subheader("🎯 Suggested Job Roles")

            roles = {
                "Web Developer": ["HTML", "CSS", "JavaScript"],
                "Python Developer": ["Python"],
                "Java Developer": ["Java"],
                "Data Analyst": ["Python", "SQL"]
            }

            suggested_roles = []

            for role, required_skills in roles.items():
                if any(
                    skill.lower() in resume_text.lower()
                    for skill in required_skills
                ):
                    suggested_roles.append(role)

            if suggested_roles:
                for role in suggested_roles:
                    st.write(f"✨ {role}")
            else:
                st.write(
                    "Add relevant technical skills to help identify "
                    "suitable job roles."
                )

            st.divider()
            st.subheader("💡 Resume Improvement Suggestions")
            st.markdown("#### 💪 Resume Strengths")

            if found:
                st.write(
                    "Your resume contains these relevant skills: "
                    + ", ".join(found) + "."
                )
            else:
                st.write(
                    "No matching skills were found. Include relevant "
                    "skills you genuinely possess."
                )

            st.markdown("#### 🔍 Resume Weaknesses")

            if missing:
                st.write(
                    "Your resume does not mention these job requirements: "
                    + ", ".join(missing) + "."
                )
            else:
                st.success("No missing skills were identified.")

            st.subheader("✦ Personalized Resume Feedback")

            if found:
                st.write(
                    "Good job! Your resume mentions these relevant skills: "
                    + ", ".join(found) + "."
                )

            if missing:
                st.write(
                    "Consider learning these skills: "
                    + ", ".join(missing) + ". Add them to your resume "
                    "only after gaining the relevant knowledge."
                )

            if len(resume_text.split()) < 100:
                st.write(
                    "Your resume contains relatively little text. "
                    "Consider adding relevant project details and achievements."
                )
            else:
                st.write(
                    "Review your project descriptions. Explain what you "
                    "built, which technologies you used, and what you achieved."
                )

            report = f"""
AI RESUME ANALYZER REPORT

Matching Skills: {', '.join(found) if found else 'None'}

Skills to Learn: {', '.join(missing) if missing else 'None'}

Suggested Job Roles: {
    ', '.join(suggested_roles) if suggested_roles else 'None identified'
}

Resume Match Percentage: {
    f'{match:.0f}%' if total_skills > 0 else 'Not available'
}

Resume Improvement Suggestions:
- Highlight relevant skills and projects.
- Add specific achievements where appropriate.
- Include skills in your resume only when you genuinely have them.
"""

            st.download_button(
                label="📥 Download Analysis Report",
                data=report,
                file_name="resume_analysis_report.txt",
                mime="text/plain",
                use_container_width=True
            )

        else:
            st.warning(
                "Please upload your resume and enter a job description."
            )



elif page == "About":

    st.title("✨ About ResumeAI")

    st.subheader("Helping you take the next step in your career.")

    st.write(
        "ResumeAI helps users compare resume skills with job "
        "descriptions, identify missing skills, explore suggested "
        "job roles, and review practical improvement suggestions."
    )


    st.subheader("✨ Our Purpose")

    st.write(
        "Our goal is to make resume improvement simpler by giving "
        "users an accessible way to review their skills against "
        "the requirements of a job."
    )

    st.subheader("🚀 What You Can Do")

    st.markdown("""
    - Compare your resume with a job description.
    - Identify matching and missing skills.
    - Explore suggested job roles.
    - Review personalized resume feedback.
    - Download your analysis report.
    """)



st.markdown("""
<div class="footer">
    ✦ ResumeAI | Built with Streamlit
    <br><br>
    Your career. Your next chapter.
</div>
""", unsafe_allow_html=True)

