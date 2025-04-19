def is_valid_immatriculation(text):
    """Check if text matches the expected immatriculation format."""
    if not text or "|" not in text:
        return False
    parts = [part.strip() for part in text.split("|")]
    return (len(parts) == 3 and
            parts[0].isdigit() and
            len(parts[1]) == 1 and
            parts[2].isdigit())
