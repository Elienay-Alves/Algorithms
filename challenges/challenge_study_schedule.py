def study_schedule(permanence_period, target_time):
    students = 0

    try:
        for on, off in permanence_period:
            if on <= target_time <= off:
                students += 1

    except (TypeError, ValueError, AssertionError):
        return None

    return students
