
def solve_part_1(outputs_group):
    res = 0

    for outputs in outputs_group:
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                res += 1

    return res

if __name__ == '__main__':
    with open('input_01.txt') as f:
        patterns_group = []
        outputs_group = []

        for line in f.readlines():
            line = line.strip().split(' | ')

            patterns_group.append(line[0].strip().split(' '))
            outputs_group.append(line[1].strip().split(' '))
            
        print(solve_part_1(outputs_group))