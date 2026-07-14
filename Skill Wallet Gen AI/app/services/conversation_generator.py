def generate_conversation_starters(
        profession,
        interests
):

    suggestions = []


    for interest in interests:

        suggestions.append(
            f"What projects have you worked on related to {interest}?"
        )


        suggestions.append(
            f"What trends do you see in {interest}?"
        )


    suggestions.append(
        f"What challenges do you face as a {profession}?"
    )


    return suggestions[:10]
