# Convert between decimal and gumatj(base 5) bases, and gumatj calculations

def gumatj_to_decimal(num):
    return int(str(num), 5)


def decimal_to_gumatj(num):
    return int(str(gumatj_to_decimal(num)), 10)


def gumatj_add(num_1, num_2):
    return decimal_to_gumatj(gumatj_to_decimal(num_1) + gumatj_to_decimal(num_2))


def gumatj_multiply(num_1, num_2):
    return decimal_to_gumatj(gumatj_to_decimal(num_1) * gumatj_to_decimal(num_2))