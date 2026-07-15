import json
import os

HISTORY_FILE = "history.json"


def save_history(data):
    print("=== save_history() called ===")
    print("Current Working Directory:", os.getcwd())

    history = []

    if os.path.exists(HISTORY_FILE):
        print("history.json exists")
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)
        except Exception as e:
            print("Read Error:", e)
            history = []
    else:
        print("history.json does NOT exist")

    history.append(data)

    print("Saving to:", os.path.abspath(HISTORY_FILE))

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

    print("History saved successfully")


def get_history():
    print("Reading from:", os.path.abspath(HISTORY_FILE))

    if not os.path.exists(HISTORY_FILE):
        print("history.json not found")
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
