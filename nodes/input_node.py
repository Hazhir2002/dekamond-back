def input_node(state):
    """Validates the input we recieve"""
    data = state["input_data"]
    required_days = ("today", "yesterday")
    for day in required_days:
        if day not in data:
            raise KeyError(f"Missing required day ‘{day}’ in input")

        block = data[day]
        if not isinstance(block, dict):
            raise TypeError(f"Expected {day} to be a dict, got {type(block)}")

        for field in ("revenue", "cost", "customers"):
            if field not in block:
                raise KeyError(f"Missing field ‘{field}’ in {day} data")

    return state
