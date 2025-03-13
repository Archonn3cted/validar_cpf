def validate_cpf(cpf: str) -> bool:
    if not cpf:
        return False

    cpf_str = str(cpf)

    if len(cpf_str) != 11:
        return False

    equal_digits = all(digit == cpf_str[0] for digit in cpf_str)
    if equal_digits:
        return False

    numbers = cpf_str[:9]
    digits = cpf_str[9:]

    sum_ = 0
    for i in range(10, 1, -1):
        sum_ += int(numbers[10 - i]) * i
    result = 0 if sum_ % 11 < 2 else 11 - (sum_ % 11)
    if result != int(digits[0]):
        return False

    numbers = cpf_str[:10]
    sum_ = 0
    for i in range(11, 1, -1):
        sum_ += int(numbers[11 - i]) * i
    result = 0 if sum_ % 11 < 2 else 11 - (sum_ % 11)
    if result != int(digits[1]):
        return False

    return True