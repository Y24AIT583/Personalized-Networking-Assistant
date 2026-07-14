def generate_recommendations(
        interests,
        skills,
        profession
):

    recommendations = []


    if "Artificial Intelligence" in interests:
        recommendations.append(
            "AI Developer"
        )


    if "Machine Learning" in interests:
        recommendations.append(
            "ML Engineer"
        )


    if "Cloud Computing" in interests:
        recommendations.append(
            "Cloud Engineer"
        )


    if not recommendations:
        recommendations.append(
            "Technology Professional"
        )


    return recommendations
