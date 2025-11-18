def split_before_each_uppercases(formula):
    if not formula:
        return []

    splitted_formula = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            splitted_formula.append(formula[start:i])
            start = i

    splitted_formula.append(formula[start:])
    return splitted_formula


def split_at_first_digit(formula):
    if not formula:
        return "", 1

    for i, ch in enumerate(formula):
        if ch.isdigit():
            k = i
            while k < len(formula) and formula[k].isdigit():
                k += 1
            prefix = formula[:i]
            number_part = int(formula[i:k])
            return prefix, number_part

    return formula, 1
