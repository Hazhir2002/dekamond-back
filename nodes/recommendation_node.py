def recommendation_node(state):
    """Recommendation node that outputs advice based on the calculations (e.g., warn if CAC increased, suggest increasing marketing budget if sales grew)."""
    metrics = state["metrics"]
    recommendations = []
    alerts = []

    if metrics["profit"] < 0:
        alerts.append("Warning: Negative profit")
        recommendations.append("Reduce costs to improve profitability.")

    if metrics["cac_change_percent"] > 20:
        alerts.append("Alert: CAC increased by more than 20%")
        recommendations.append("Review marketing campaigns to reduce CAC.")

    if metrics["revenue_change_percent"] > 10:
        recommendations.append(
            "Consider increasing advertising budget to boost growth."
        )

    state["summary"] = {
        "profit": metrics["profit"],
        "alerts": alerts,
        "recommendations": recommendations,
    }

    return state
