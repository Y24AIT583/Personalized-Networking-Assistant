import json
import os

FEEDBACK_FILE = "feedback.json"


def save_feedback(data):
    """
    Save user feedback to a JSON file.
    """

    feedback = []

    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
                feedback = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            feedback = []

    feedback.append(data)

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
        json.dump(feedback, file, indent=4)
