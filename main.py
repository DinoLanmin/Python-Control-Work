import itertools

# Pytho Control Work 12.06.2024

numbers_a = [2, 0, 509, 23]
numbers_b = [45, 0, 14, 8, 1]
numbers_case = []

numbers_case.append(''.join(map(str, sorted(numbers_a))))

numbers_case.append(''.join(map(str, sorted(numbers_a, reverse=True))))

numbers_case.append(''.join(map(str, sorted(numbers_b))))

numbers_case.append(''.join(map(str, sorted(numbers_b, reverse=True))))

print(*numbers_case)
