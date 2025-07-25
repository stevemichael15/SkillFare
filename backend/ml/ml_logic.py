
# backend/ml_logic.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data for ML domain prediction
sample_data = [
    ("Web Development", "html css javascript frontend backend fullstack responsive", "Web Dev"),
    ("Machine Learning", "model training dataset features regression classification", "ML"),
    ("Data Science", "data visualization statistics pandas analysis insight", "Data Science"),
    ("Mobile Apps", "android ios kotlin swift reactnative flutter", "Mobile Dev"),
    ("Cybersecurity", "encryption firewall network penetration secure", "Security"),
    ("Cloud", "aws gcp azure cloud functions storage deployment", "Cloud"),
    ("DevOps", "docker ci/cd automation kubernetes pipelines monitoring", "DevOps"),
]

# Train ML model for domain prediction
X_train = [desc for _, desc, _ in sample_data]
y_train = [label for _, _, label in sample_data]
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_vec, y_train)

# Predict domain from user free-text input
def predict_domain(user_text):
    X_user = vectorizer.transform([user_text])
    predicted = model.predict(X_user)
    return predicted[0]

# Mapping domain key to suggestions
domain_map = {
    "Web Development": "Web Dev",
    "Machine Learning": "ML",
    "Data Science": "Data Science",
    "Mobile Apps": "Mobile Dev",
    "Cybersecurity": "Security",
    "Cloud": "Cloud",
    "DevOps": "DevOps",
    "Game Dev": "Game Dev",
    "AR/VR": "ARVR",
    "Open Source": "Open Source",
    "UI/UX Design": "UIUX",
    "Blockchain": "Blockchain"
}

# Suggestions database
suggestions = {
    "Web Dev": {
        "career": "Frontend/Backend Engineer, Fullstack Developer",
        "roadmap": "Start with HTML → CSS → JS → Frameworks (React, Node)",
        "projects": ["Portfolio Website", "Blog CMS"],
        "resume_tip": "Showcase frontend/backend projects on GitHub with live links"
    },
    "Blockchain": {
      "career": "Blockchain Developer, Smart Contract Engineer, Web3 Architect",
      "roadmap": "Learn blockchain basics → Smart contracts (Solidity) → DApps (Ethereum, Polygon)",
      "projects": ["NFT Marketplace", "Decentralized Voting System"],
      "resume_tip": "Mention hands-on Solidity projects and deployments to testnets/mainnet"
    },
    "ML": {
        "career": "ML Engineer, Data Analyst, AI Engineer",
        "roadmap": "Start with NumPy → Pandas → Scikit-learn → Projects",
        "projects": ["Spam Classifier", "Stock Prediction Model"],
        "resume_tip": "Highlight ML models with performance metrics"
    },
    "Data Science": {
        "career": "Data Scientist, BI Analyst, Research Analyst",
        "roadmap": "Statistics → Data Wrangling → Visualization → ML Basics",
        "projects": ["Sales Dashboard", "Customer Segmentation"],
        "resume_tip": "Include visualizations and insights drawn from data"
    },
    "Mobile Dev": {
        "career": "Android/iOS Developer, Flutter Engineer",
        "roadmap": "Choose platform → Learn UI frameworks → Deploy apps",
        "projects": ["Weather App", "Expense Tracker"],
        "resume_tip": "Publish your apps on the Play Store/App Store"
    },
    "Security": {
        "career": "Penetration Tester, Security Analyst",
        "roadmap": "Networking → Cryptography → Ethical Hacking",
        "projects": ["Password Vault", "Vulnerability Scanner"],
        "resume_tip": "Certifications like CEH or OSCP boost your profile"
    },
    "Cloud": {
        "career": "Cloud Engineer, Solutions Architect",
        "roadmap": "Understand cloud models → Services (AWS/GCP) → Deployments",
        "projects": ["Serverless App", "Cloud Storage API"],
        "resume_tip": "Mention hands-on with real cloud deployments"
    },
    "DevOps": {
        "career": "DevOps Engineer, Automation Specialist",
        "roadmap": "Learn Docker → CI/CD → Monitoring Tools",
        "projects": ["CI/CD pipeline", "Kubernetes cluster"],
        "resume_tip": "Mention automations and monitoring tools"
    },
    "Game Dev": {
        "career": "Game Developer, Unity/Unreal Developer",
        "roadmap": "Learn a game engine → Design mechanics → Build & deploy games",
        "projects": ["2D Platformer", "3D Multiplayer Game"],
        "resume_tip": "Showcase game demos and GitHub repositories with gameplay videos"
    },
    "ARVR": {
        "career": "AR/VR Developer, Immersive Experience Designer",
        "roadmap": "Learn Unity/Unreal → Explore ARKit/ARCore → Build immersive apps",
        "projects": ["Virtual Tour App", "AR Furniture Placement Tool"],
        "resume_tip": "Include GIFs/demos of immersive projects in your portfolio"
    },
    "Open Source": {
        "career": "Open Source Contributor, Community Maintainer",
        "roadmap": "Pick a project → Understand the codebase → Contribute regularly",
        "projects": ["GitHub Contribution Tracker", "Open Source Bug Fixes"],
        "resume_tip": "Mention accepted PRs and recognized contributions"
    },
    "UIUX": {
        "career": "UI/UX Designer, Product Designer",
        "roadmap": "Learn Figma/Sketch → Study design systems → Build case studies",
        "projects": ["App Redesign", "User Flow Prototype"],
        "resume_tip": "Link to design portfolios and user research insights"
    }
}



# Main analysis function: can accept either a list of domains or a user_text for ML prediction
def generate_analysis(domains=None, skill_level="Beginner", user_text=None):
    analysis = {}

    # Normalize skill level input
    skill_level = (skill_level or "Beginner").strip().capitalize()
    if skill_level not in ["Beginner", "Intermediate", "Expert"]:
        skill_level = "Beginner"

    # If user_text is provided, use ML to predict the most relevant domain
    if user_text and (not domains or len(domains) == 0):
        predicted_domain = predict_domain(user_text)
        # Map ML label back to display name
        reverse_map = {v: k for k, v in domain_map.items()}
        domain_name = reverse_map.get(predicted_domain, predicted_domain)
        domains = [domain_name]

    if not domains:
        return {"error": "No domains or user text provided."}

    for domain in domains:
        key = domain_map.get(domain, None)
        base = suggestions.get(key, {
            "career": "Explore diverse opportunities in this domain.",
            "roadmap": "Start with fundamentals and explore specialized paths.",
            "projects": ["Project A", "Project B"],
            "resume_tip": "Mention relevant tools, projects, and certifications."
        })

        # Generate skill-level adjusted suggestions
        if skill_level == "Beginner":
            roadmap = "Focus on foundational concepts and beginner-friendly tutorials."
            projects = [f"Intro to {domain}", f"{domain} Starter App"]
        elif skill_level == "Intermediate":
            roadmap = base["roadmap"]
            projects = base["projects"]
        else:  # Expert
            roadmap = f"Advance into real-world projects, architecture design, and lead roles in {domain}."
            projects = [f"{domain} Scalable System", f"{domain} AI-Integrated Platform"]

        analysis[domain] = {
            "career": base["career"],
            "roadmap": roadmap,
            "projects": projects,
            "resume_tip": base["resume_tip"] + f" Emphasize your {skill_level.lower()} proficiency."
        }

    return analysis
