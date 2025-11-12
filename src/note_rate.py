def rate_note(note: int) -> str:
    if note == 16:
        return "excellent"
    if note < 10:
        return "unsuccessful"
    if note >= 10 and note < 12:
        return "acceptable"
    if note >= 12 and note < 14:
       return "good"
    return "very good"