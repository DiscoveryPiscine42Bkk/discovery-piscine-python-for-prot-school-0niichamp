array = [2, 8, 9, 48, 8, 22, -12, 2]
new = [number + 2 for number in array if number > 5]
new12 = set(new)
print(array)
print(new12)