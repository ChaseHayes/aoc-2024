from re import match

with open('puzzle1_input.txt', 'r') as file:
    lines = file.read().split('\n')

column1 = []
column2 = []

for line in lines:
    if line == '':
        continue

    matched = match(r'(\d+)\s+(\d+)', line)

    column1.append(int(matched.group(1)))
    column2.append(int(matched.group(2)))

column1_sorted = sorted(column1)
column2_sorted = sorted(column2)

total_distance = 0

for i in range(len(column1_sorted)):
    total_distance += abs(column2_sorted[i] - column1_sorted[i])

print(total_distance)
