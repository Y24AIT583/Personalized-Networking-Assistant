def generate_conversation_topics(event_topics, user_interests):
    """
    Generate personalized conversation starters
    for professional networking interactions.
    """

    suggestions = []

    # Generate questions from event topics
    for topic in event_topics:
        suggestions.append(
            f"What inspired you to explore {topic}?"
        )

        suggestions.append(
            f"How do you see {topic} impacting the industry in the future?"
        )

        suggestions.append(
            f"What are some interesting developments you have noticed in {topic}?"
        )

    # Generate questions from user's interests
    for interest in user_interests:
        suggestions.append(
            f"I noticed you're interested in {interest}. "
            f"What projects or experiences have you had in this area?"
        )

        suggestions.append(
            f"What skills are you currently building related to {interest}?"
        )

    # Return maximum 10 conversation starters
    return suggestions[:10]
