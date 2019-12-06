from collections import Counter


def solve():
    number_of_passwords = 0
    number_of_passwords_2 = 0
    for i in range(236491, 713787):
        digits = [int(s) for s in str(i)]
        has_pair = False
        is_decreasing = True
        counts = Counter(digits)
        for digit in range(1, len(digits)):
            if digits[digit] < digits[digit - 1]:
                is_decreasing = False
                break
            if digits[digit - 1] == digits[digit]:
                has_pair = True

        if has_pair and is_decreasing:
            number_of_passwords += 1

            if 2 in counts.values():
                number_of_passwords_2 += 1

    return number_of_passwords, number_of_passwords_2
