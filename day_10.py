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


if __name__ == "__main__":
    pass
