input_file = __file__.split('\\')[-1].replace('.py', '') + "_input.txt"


def process_input_line(line):
    # light red bags | contain | 1 bright white bag,| 2 muted yellow bags.|
    line = line.strip().replace('bags', '').replace('bag', '')
    line = line.replace('.', '')
    line = line.split('contain')
    container = line[0].strip()
    content = line[1].strip()
    return container, content


input_lines = dict()
with open(input_file) as f:
    while True:
        raw_line = f.readline()
        if raw_line:
            container, content = process_input_line(raw_line)
            input_lines[container] = (content)
        else:
            break
max_lines = len(input_lines)


def recursion(bag):
    n_bag = 1
    if 'no other' in input_lines[bag]:
        pass
    else:
        entries = input_lines[bag]
        entries = entries.split(',')
        for e in entries:
            e = e.strip()
            n_bag += int(e[0])*recursion(e[2:])
    return n_bag


if __name__ == "__main__":
    pre_answer = -1
    answer = 0
    target = 'shiny gold'
    valid_container = list()
    valid_container.append(target)
    while answer != pre_answer:
        pre_answer = answer
        for i in input_lines:
            for v in valid_container:
                if (v in input_lines[i] and
                        i.replace(' bags', '') not in valid_container):
                    valid_container.append(i.replace(' bags', ''))
        answer = len(valid_container)
        print(answer)
    print(answer - 1)

    print(recursion(target) - 1)
