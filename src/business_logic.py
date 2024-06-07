def assess_behavior(attention_span, social_interaction, activity_level):
    # Enhanced assessment logic with additional parameters
    def calculate_risk(attention_span, social_interaction, activity_level):
        # Weighted risk calculation based on attention span, social interaction, and activity level
        risk_score = 0

        # Attention span impact
        if attention_span < 30:
            risk_score += 3
        elif attention_span < 60:
            risk_score += 2
        else:
            risk_score += 1

        # Social interaction impact
        if social_interaction == "Low":
            risk_score += 3
        elif social_interaction == "Medium":
            risk_score += 2
        else:
            risk_score += 1

        # Activity level impact
        if activity_level < 3:
            risk_score += 3
        elif activity_level < 7:
            risk_score += 2
        else:
            risk_score += 1

        return risk_score

    risk_score = calculate_risk(attention_span, social_interaction, activity_level)

    if risk_score >= 7:
        risk_level = "High"
    elif risk_score >= 4:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "Attention Span": attention_span,
        "Social Interaction Level": social_interaction,
        "Activity Level": activity_level,
        "Risk Level": risk_level,
        "Risk Score": risk_score,
    }
