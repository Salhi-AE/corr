def rate_note(note: int) -> str:
    if note == 14:
       return "very good"
    if note < 10:
        return "unsuccessful"
    if note >= 10 and note < 12:
        return "acceptable"
    return "good"