inp = "day_01_input.txt"
with open(inp) as f:
    entries = f.readlines()


class Break(Exception):
    pass


try:
    for i in range(len(entries)):
        for j in range(len(entries)):
            if int(entries[i]) + int(entries[j]) == 2020:
                answer = int(entries[i])*int(entries[j])
                raise Break
except Break:
    print("Part 1 = ", answer)

try:
    for i in range(len(entries)):
        for j in range(len(entries)):
            for k in range(len(entries)):
                if int(entries[i]) + int(entries[j]) + int(entries[k]) == 2020:
                    answer = int(entries[i])*int(entries[j])*int(entries[k])
                    raise Break
except Break:
    print("Part 2 = ", answer)
