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
    Lightweight profile analyzer based on keyword matching.
    Suitable for deployment on free hosting platforms.
    """

    description = description.lower()

    interests = []

    for topic in CANDIDATE_INTERESTS:
        if topic.lower() in description:
            interests.append(topic)

    # If nothing is detected, return a few general topics
    if not interests:
        interests = [
            "Software Development",
            "Artificial Intelligence",
            "Machine Learning"
        ]

    return interests