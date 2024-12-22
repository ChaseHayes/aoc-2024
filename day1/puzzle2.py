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

similarity_score = 0

for col1_val in column1:
    count_of_matches = 0

    for col2_val in column2:
        if col1_val == col2_val:
            count_of_matches += 1

    similarity_score += col1_val * count_of_matches

print(similarity_score)
