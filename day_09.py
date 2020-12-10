input_file = "day_09_input.txt"
entries = list()
with open(input_file) as f:
    while True:
        n = f.readline()
        if n:
            entries.append(int(n))
        else:
            break
max_rows = len(entries)


window_size = 25

i = window_size
while i < max_rows:
    target_num = entries[i]
    addends = entries[i - window_size:i]
    found = False
    for a in addends:
        missing_value = target_num - a
        if (missing_value in addends and
                missing_value != a):
            found = True
            break
    if not found:
        print("Part 1 = ", target_num)
        break
    i += 1

i = 0
found = False
while i < max_rows:
    num_set = list()
    j = 0
    while (j + i) < max_rows:
        num_set.append(entries[i + j])
        if len(num_set) > 2 and sum(num_set) == target_num:
            print("Part 2 = ", min(num_set) + max(num_set))
            found = True
            break
        j += 1
    if found:
        break
    i += 1
