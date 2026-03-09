def calculate_ats_score(resume_text: str) -> int:
    text = resume_text.lower()

    # Skills relevance (0–30)
    skills_keywords = [
        "python",
        "java",
        "c++",
        "c#",
        "javascript",
        "typescript",
        "react",
        "node",
        "django",
        "flask",
        "sql",
        "mysql",
        "postgres",
        "mongodb",
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "machine learning",
        "data science",
        "git",
        "rest api",
        "microservices",
    ]
    skills_hits = sum(1 for kw in skills_keywords if kw in text)
    skills_score = min(skills_hits, 10) / 10 * 30  # cap at 30

    # Projects mentioned (0–20)
    project_keywords = ["project", "projects", "github", "portfolio", "case study", "hackathon"]
    project_hits = sum(text.count(kw) for kw in project_keywords)
    if project_hits == 0:
        projects_score = 0
    elif project_hits == 1:
        projects_score = 8
    elif project_hits == 2:
        projects_score = 14
    else:
        projects_score = 20

    # Education section (0–20)
    education_keywords = [
        "education",
        "bachelor",
        "master",
        "b.tech",
        "b.e",
        "bsc",
        "msc",
        "phd",
        "degree",
        "university",
        "college",
    ]
    edu_hits = sum(1 for kw in education_keywords if kw in text)
    if edu_hits == 0:
        education_score = 0
    elif edu_hits == 1:
        education_score = 10
    else:
        education_score = 20

    # Experience or internships (0–20)
    experience_keywords = [
        "experience",
        "work experience",
        "professional experience",
        "internship",
        "intern",
        "software engineer",
        "developer",
        "analyst",
        "consultant",
    ]
    exp_hits = sum(1 for kw in experience_keywords if kw in text)
    if exp_hits == 0:
        experience_score = 0
    elif exp_hits == 1:
        experience_score = 10
    else:
        experience_score = 20

    # Resume length / formatting (0–10)
    words = text.split()
    word_count = len(words)
    if 200 <= word_count <= 1000:
        length_score = 10
    elif 100 <= word_count < 200 or 1000 < word_count <= 1500:
        length_score = 7
    elif 50 <= word_count < 100 or 1500 < word_count <= 2000:
        length_score = 4
    else:
        length_score = 1 if word_count > 0 else 0

    total_score = skills_score + projects_score + education_score + experience_score + length_score
    return int(max(0, min(100, round(total_score))))

