# SkillFare — Personalized Tech Roadmaps & Project Generator

**SkillFare** is a smart and modern web platform that helps users explore and grow in their chosen tech domains. It generates personalized learning paths, project ideas, and resume tips based on selected interests and skill levels (Beginner, Intermediate, Expert).

---

## Features

- **Domain Selection** — Choose from domains like Web Dev, Machine Learning, Data Science, and more.
- **Skill-Based Analysis** — Personalized suggestions for Beginner, Intermediate, or Expert level users.
- **Career Insights** — Get curated career insights and what to focus on next.
- **Project Ideas** — Instantly receive tailored project ideas with implementation guidance.
- **Resume Tips** — Boost your resume with domain-specific additions.
- **PDF Export** — Download the full analysis in a clean, aesthetic PDF format.
- **Save & Update** — Save user preferences and regenerate anytime.
- **Modern UI** — Neon-themed responsive design with smooth UX.

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/skillfare.git
cd skillfare
```

### 2. Create a virtual environment

```bash
python -m venv .env
.env\Scripts\activate  # On Windows
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Setup wkhtmltopdf (for PDF feature)

```bash
Download from: [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
Set the executable path in backend/app.py or wherever pdfkit.configuration() is used****
```

### 5. Run the app

```bash
python run.py
```


## Project Structure

```bash
├── backend/
│   ├── templates/
│   ├── static/
│   ├── routes/
│   └── app.py
├── ml_logic/
│   └── logic.py
├── run.py
├── requirements.txt
└── README.md
```
## Upcoming Features
- User login & persistent analysis history
- More domains and roadmap APIs
- AI-generated smarter recommendations
- Feedback-based roadmap refinement

## License
This project is licensed under the MIT License.

## Contributing
We welcome contributions! Fork the repo, open an issue, or submit a pull request.

## Let's Connect!

- Email: [stevemichael681@gmail.com](mailto:stevemichael681@gmail.com)  
- LinkedIn: [Steve Michael](https://www.linkedin.com/in/steve-michael-512666222)  
- GitHub: [stevemichael15](https://github.com/stevemichael15)  
- Kaggle: [steve92510](https://www.kaggle.com/steve92510)

