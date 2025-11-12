def rate_note(note: int) -> str:
    if note == 12:
        return "good"
    if note < 10:
        return "unsuccessful"
    return "acceptable"