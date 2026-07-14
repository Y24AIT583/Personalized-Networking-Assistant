import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="personalized-networking-assistant"
)


def verify_topic(query: str):
    """
    Verify a professional topic using Wikipedia.
    Returns a short summary if the topic exists.
    """

    page = wiki.page(query)

    if page.exists():
        return page.summary[:500]

    return "No verified information found for the given topic."
