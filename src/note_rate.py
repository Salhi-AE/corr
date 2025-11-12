def rate_note(note: int) -> str:

    if note < 10:
        return "unsuccessful"
    if note >= 10 and note < 12:
        return "acceptable"
    if note >= 12 and note < 14:
       return "good"
    if note >= 14 and note < 16:
        return "very good"
    return "excellent"