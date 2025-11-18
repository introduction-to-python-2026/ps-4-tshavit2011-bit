def split_at_digit(formula: str):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            j = i
            while j < len(formula) and formula[j].isdigit():
                j += 1
            return formula[:i], int(formula[i:j])
    return formula, 1


def split_before_each_uppercase(formula: str):
    if not formula:
        return []
    parts = []
    current = ""
    for ch in formula:
        if ch.isupper() and current:
            parts.append(current)
            current = ch
        else:
            current += ch
    if current:
        parts.append(current)
    return parts
