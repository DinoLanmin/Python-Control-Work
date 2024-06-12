# Pytho Control Work 12.06.2024

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = ['a', 'b', 'c', 'd', 'f', 'g', 'k', 'l']
c = ''

for number, letter in zip(a, b):
    c += str(number) + ' ' + letter + ' '

print(c)
