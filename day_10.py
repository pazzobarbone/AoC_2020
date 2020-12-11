input_file = __file__.split('\\')[-1].replace('.py', '') + "_input.txt"


def process_input_line(line):
    line = line.strip()
    return int(line)


input_lines = list()
with open(input_file) as f:
    while True:
        raw_line = f.readline()
        if raw_line:
            input_lines.append(process_input_line(raw_line))
        else:
            break
max_lines = len(input_lines)


def tribonacci(n):
    last_3 = [0, 0, 1]
    i = 0
    while i != n:
        new = sum(last_3)
        last_3.append(new)
        last_3.pop(0)
        i += 1
    return last_3[-1]

if __name__ == "__main__":
    input_range = range(1,4)
    current_rating = 0
    j_diff_1 = 0
    j_diff_2 = 0
    j_diff_3 = 0
    arrangements = 1
    input_lines.append(max(input_lines)+3)
    while input_lines:
        for i in input_range:
            if current_rating + i in input_lines:
                if i == 1:
                    j_diff_1 +=1
                elif i == 2:
                    j_diff_2 +=1
                elif i == 3:
                    j_diff_3 +=1
                    arrangements *= tribonacci(j_diff_1)
                    j_diff_1 = 0
                input_lines.remove(current_rating + i)
                current_rating += i
                break
    #print(j_diff_1*(j_diff_3))
    print(arrangements)
