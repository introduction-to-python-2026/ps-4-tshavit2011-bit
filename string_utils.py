
 def split_at_first_digit(formula):
    digit = 1

    for ch in formula[1:]:
        if ch.isdigit():
            break
        else:
            digit += 1

    if digit == len(formula):
        return formula, 1

    prefix = formula[:digit]
    number = int(formula[digit:])
    return prefix, number    


def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
