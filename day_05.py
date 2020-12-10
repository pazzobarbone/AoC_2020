inp = "day_05_input.txt"
entries = list()
with open(inp) as f:
    entries = f.readlines()
max_rows = len(entries)

boarding_passes = list()

max_row = 0
max_col = 0
for e in entries:
    row_id = e[0:7]
    row = list()
    for a in range(128):
        row.append(a)
    i = 127
    for r in row_id:
        i = i // 2
        if r == 'F':
            row = row[0:i+1]
        else:
            row = row[i+1:]
    row = row[0]
    if row > max_row:
        max_row = row

    col_id = e[7:].strip()
    col = list()
    for a in range(8):
        col.append(a)
    i = 7
    for r in col_id:
        i = i // 2
        if r == 'L':
            col = col[0:i+1]
        else:
            col = col[i+1:]
    col = col[0]
    if col > max_col:
        max_col = col

    boarding_passes.append(row*8 + col)

max_id = max(boarding_passes)
for i in range(max_col + 1, max_row * max_col - max_col):
    if (i not in boarding_passes
            and i + 1 in boarding_passes
            and i - 1 in boarding_passes):
        break
print("Part 1 = ", max(boarding_passes))
print("Part 2 = ", i)
