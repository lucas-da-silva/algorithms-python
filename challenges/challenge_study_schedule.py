def study_schedule(permanence_period: list[tuple], target_time: int) -> int:
    best_period = 0

    try:
        for entry, leave in permanence_period:
            if entry <= target_time <= leave:
                best_period += 1
    except TypeError:
        return None

    return best_period
