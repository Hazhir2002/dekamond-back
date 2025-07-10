def processing_node(state):
    """calculates key metrics such as profit, simple CAC, and compares today’s sales/costs with the previous day."""
    data = state["input_data"]

    today = data["today"]
    yesterday = data["yesterday"]

    profit = today["revenue"] - today["cost"]
    prev_profit = yesterday["revenue"] - yesterday["cost"]

    profit_change = (
        ((profit - prev_profit) / abs(prev_profit)) * 100 if prev_profit else 0
    )
    revenue_change = (
        ((today["revenue"] - yesterday["revenue"]) / yesterday["revenue"]) * 100
        if yesterday["revenue"]
        else 0
    )
    cost_change = (
        ((today["cost"] - yesterday["cost"]) / yesterday["cost"]) * 100
        if yesterday["cost"]
        else 0
    )

    cac_today = today["cost"] / today["customers"] if today["customers"] else 0
    cac_yesterday = (
        yesterday["cost"] / yesterday["customers"] if yesterday["customers"] else 0
    )
    cac_change = (
        ((cac_today - cac_yesterday) / cac_yesterday) * 100 if cac_yesterday else 0
    )

    state.update(
        {
            "metrics": {
                "profit": profit,
                "profit_change_percent": round(profit_change, 2),
                "revenue_change_percent": round(revenue_change, 2),
                "cost_change_percent": round(cost_change, 2),
                "cac_today": round(cac_today, 2),
                "cac_change_percent": round(cac_change, 2),
            }
        }
    )

    return state
