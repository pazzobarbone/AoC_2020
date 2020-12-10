import copy
inp = "day_06_input.txt"
entries = list()
with open(inp) as f:
    entries = f.readlines()
if entries[-1] != '\n':
    entries.append('\n')
max_rows = len(entries)


current_group = list()
yes_count = 0
new_group = True
for entry in entries:
    if entry == '\n':
        yes_count += len(current_group)
        current_group = list()
        new_group = True
    else:
        entry = entry.strip()
        if new_group:
            new_group = False
            for c in entry:
                current_group.append(c)
        else:
            upd_group = copy.deepcopy(current_group)
            for c in current_group:
                if c not in entry:
                    upd_group.remove(c)
            current_group = copy.deepcopy(upd_group)

print("Part 2 = ", yes_count)
