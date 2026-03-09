import streamlit as st

from pdf_parser import extract_text_from_pdf
from ats_score import calculate_ats_score
from ai_analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# Minimal, professional styling
st.markdown(
    """
<style>
.stApp {
    background-color: #f5f5f7;
    color: #111827;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.subtitle {
    text-align: center;
    font-size: 0.95rem;
    color: #4b5563;
    margin-bottom: 1.5rem;
}
.main-card {
    background-color: #ffffff;
    padding: 1.75rem;
    border-radius: 0.75rem;
    border: 1px solid #e5e7eb;
}
.stButton>button {
    background-color: #2563eb;
    color: #ffffff;
    border-radius: 0.5rem;
    border: 1px solid #1d4ed8;
}
.stButton>button:hover {
    background-color: #1d4ed8;
}
</style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1 style='text-align:center; margin-bottom:0.25rem;'>AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Upload your resume to get ATS score, skill insights, and improvement suggestions.</p>",
    unsafe_allow_html=True,
)

# Upload section (centered card)
with st.container():
    left_spacer, upload_col, right_spacer = st.columns([1, 2, 1])
    with upload_col:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        st.markdown("</div>", unsafe_allow_html=True)

# Main logic
if uploaded_file is not None:
    with st.container():
        st.success("Resume uploaded successfully.")
        resume_text = extract_text_from_pdf(uploaded_file)
        ats_score = calculate_ats_score(resume_text)

        left_spacer, score_col, right_spacer = st.columns([1, 2, 1])
        with score_col:
            st.subheader("ATS Score")
            st.metric("ATS Score", f"{ats_score}/100")
            st.progress(ats_score / 100.0)

    st.markdown("---")

    with st.container():
        st.subheader("AI Resume Analysis")
        with st.spinner("Analyzing your resume..."):
            prompt = f"""
            You are an expert career coach and ATS-aware resume reviewer
            for software and technology roles.

            The ATS score calculated by the system is {ats_score}/100.
            Based on this score and the resume content, analyze the resume
            and provide a concise, professional markdown report with the
            following sections and headings:

            ### Detected Skills
            - List the main technical and soft skills inferred from the resume.

            ### Recommended Job Roles
            - Bullet list of 3–5 job titles that best match this profile.

            ### Strengths
            - Bullet points highlighting what is strong or well-presented.

            ### Weaknesses
            - Bullet points describing gaps, issues, or weak areas.

            ### Suggestions for Improvement
            - Actionable, specific steps the candidate can take to improve
              both the resume and their ATS score.

            Resume:
            {resume_text}
            """
            analysis = analyze_resume(prompt)

    # Parse analysis into sections
    sections = {
        "Detected Skills": "",
        "Recommended Job Roles": "",
        "Strengths": "",
        "Weaknesses": "",
        "Suggestions for Improvement": "",
    }
    current = None
    for line in analysis.splitlines():
        stripped = line.strip()
        if stripped.startswith("### "):
            title = stripped[4:].strip()
            current = title if title in sections else None
            continue
        if current:
            sections[current] += line + "\n"

    st.markdown("---")

    # Detected skills & roles
    with st.container():
        skills_col, roles_col = st.columns(2)
        with skills_col:
            st.subheader("Detected Skills")
            content = sections["Detected Skills"].strip() or "_Not clearly detected._"
            st.markdown(content)
        with roles_col:
            st.subheader("Recommended Job Roles")
            content = sections["Recommended Job Roles"].strip() or "_No roles suggested._"
            st.markdown(content)

    st.markdown("---")

    # Strengths & weaknesses
    with st.container():
        strengths_col, weaknesses_col = st.columns(2)
        with strengths_col:
            st.subheader("Strengths")
            content = sections["Strengths"].strip() or "_No strengths identified._"
            st.markdown(content)
        with weaknesses_col:
            st.subheader("Weaknesses")
            content = sections["Weaknesses"].strip() or "_No weaknesses identified._"
            st.markdown(content)

    st.markdown("---")

    # Suggestions
    with st.container():
        st.subheader("Suggestions for Improvement")
        content = sections["Suggestions for Improvement"].strip() or "_No suggestions provided._"
        st.markdown(content)