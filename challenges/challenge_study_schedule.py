def study_schedule(
    permanence_period: list[tuple[int]], target_time: int
) -> int:
    """
    Calcula quantos estudantes estão estudando no mesmo horário alvo em um
    período de permanência (entrada e saída).
    """

    try:
        studying_at_the_same_time = sum(
            1
            for entry, leave in permanence_period
            if entry <= target_time <= leave
        )
    except TypeError:
        return None
    return studying_at_the_same_time
