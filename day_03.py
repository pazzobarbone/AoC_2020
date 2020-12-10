inp = "day_03_input.txt"
entries = list()
with open(inp) as f:
    while True:
        line = f.readline().strip()
        if line:
            entries.append(line)
        else:
            break

max_rows = len(entries)
max_col = len(entries[0])
right = 1
down = 2

row = 0
col = 0
tree_count = 0
tree_symbol = '#'
open_symbol = '.'
while row < max_rows:
    if entries[row][col] == tree_symbol:
        tree_count += 1
    row += down
    col += right
    if col >= max_col:
        col = col - max_col
print("Part 1 = ", tree_count)
print("Part 2 = ", 257*61*64*47*37)
