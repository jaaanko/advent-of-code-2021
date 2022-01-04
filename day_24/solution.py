from functools import cache

OPS = {
    'add': lambda a, b: a + b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a // b,
    'mod': lambda a, b: a % b,
    'eql': lambda a, b: 1 if a == b else 0
}


def calculate(ins_groups, digit_range):
    @cache
    def helper(i, z):
        if i == 14:
            return None if z != 0 else ''

        for digit in digit_range:
            vars = {
                'w': digit,
                'x': 0,
                'y': 0,
                'z': z,
            }

            for op, a, b in ins_groups[i]:
                vars[a] = OPS[op](vars[a], vars[b] if b in vars else int(b))

            res = helper(i+1, vars['z'])

            if res is None:
                continue

            return str(digit) + res

        return None

    return helper(0, 0)


def solve_part_1(ins_groups):
    return calculate(ins_groups, range(9, 0, -1))


def solve_part_2(ins_groups):
    return calculate(ins_groups, range(1, 10))


if __name__ == '__main__':
    with open('input_01.txt') as f:
        instructions = [line.strip().split() for line in f.readlines()]
        groups = []

        for i in range(0, len(instructions), 18):
            group = []

            for j in range(i+1, i+18):
                group.append(instructions[j])

            groups.append(group)

        print(solve_part_1(groups))
        print(solve_part_2(groups))
