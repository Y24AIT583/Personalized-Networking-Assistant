from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CANDIDATE_INTERESTS = [
    "Artificial Intelligence",
    "Machine Learning",
    "Data Science",
    "Cloud Computing",
    "Cybersecurity",
    "Software Development",
    "Web Development",
    "Mobile App Development",
    "DevOps",
    "Blockchain",
    "Internet of Things",
    "UI/UX Design",
    "Product Management",
    "Entrepreneurship",
    "Digital Marketing",
    "Finance",
    "Healthcare",
    "Education",
    "Research",
    "Open Source"
]


def analyze_profile(description: str):
    """
    Analyze a user's profile description and identify
    their professional interests.
    """

    result = classifier(
        description,
        CANDIDATE_INTERESTS,
        multi_label=True
    )

    interests = []

    for label, score in zip(
        result["labels"],
        result["scores"]
    ):
        if score > 0.30:
            interests.append(label)

    return interests
