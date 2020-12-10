inp = "day_02_input.txt"
with open(inp) as f:
    entries = f.readlines()

valid_p_counter = 0
for e in entries:
    col = e.index(':')
    letter = e[col-1]
    password = e[col+1:]
    occurrences = e[:col-1].split('-')
    occurrences = (int(occurrences[0]), int(occurrences[1]))
    i = 0
    occ = 0
    while i < len(password):
        if password[i] == letter:
            occ += 1
        i += 1
    if occurrences[0] <= occ <= occurrences[1]:
        valid_p_counter += 1
print("Part 1 = ", valid_p_counter)


valid_p_counter = 0
for e in entries:
    col = e.index(':')
    letter = e[col-1]
    password = e[col+1:]
    occurrences = e[:col-1].split('-')
    occurrences = (int(occurrences[0]), int(occurrences[1]))

    if ((password[occurrences[0]] == letter and
         not password[occurrences[1]] == letter)
            or (not password[occurrences[0]] == letter and
                password[occurrences[1]] == letter)):
        valid_p_counter += 1
print("Part 2 = ", valid_p_counter)
