def assess_behavior(attention_span, social_interaction, activity_level):
    # Simple assessment logic as a placeholder
    if attention_span < 30 and activity_level < 3:
        risk_level = "High"
    elif attention_span < 60 and activity_level < 5:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "Attention Span": attention_span,
        "Social Interaction Level": social_interaction,
        "Activity Level": activity_level,
        "Risk Level": risk_level,
    }
