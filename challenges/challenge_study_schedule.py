def study_schedule(permanence_period: list[tuple], target_time: int) -> int:
    try:
        studying_at_the_same_time = sum(
            1
            for entry, leave in permanence_period
            if entry <= target_time <= leave
        )
    except TypeError:
        return None
    return studying_at_the_same_time
