import json
import math


def can_explode(pair, layer=0):
    if type(pair) == int:
        return False

    if layer == 4:
        return True

    return can_explode(pair[0], layer+1) or can_explode(pair[1], layer+1)


def add_exploded_value(pair, id, target_id, val):
    if type(pair) == int:
        if id == target_id:
            return pair + val

        return pair

    return [add_exploded_value(pair[0], id*2, target_id, val), add_exploded_value(pair[1], id*2+1, target_id, val)]


def explode(pair):
    left_val = 0
    right_val = 0
    exploded_id = -1
    done = False
    stack = []

    def explode_helper(pair, layer=0, id=1):
        if type(pair) == int:
            stack.append(id)
            return pair

        nonlocal done

        if layer == 4 and type(pair[0]) and type(pair[1]) == int and not done:
            done = True
            nonlocal left_val, right_val, exploded_id
            left_val, right_val, exploded_id = pair[0], pair[1], id
            stack.append(id)

            return 0

        return [explode_helper(pair[0], layer+1, id*2), explode_helper(pair[1], layer+1, id*2+1)]

    pair = explode_helper(pair)

    i = stack.index(exploded_id)

    if i > 0:
        pair = add_exploded_value(pair, 1, stack[i-1], left_val)

    if i < len(stack) - 1:
        pair = add_exploded_value(pair, 1, stack[i+1], right_val)

    return pair


def can_split(pair):
    if type(pair) == int:
        return pair >= 10

    return can_split(pair[0]) or can_split(pair[1])


def split(pair):
    done = False

    def split_helper(pair):
        nonlocal done

        if type(pair) == int:
            if pair >= 10 and not done:
                done = True
                return [pair//2, math.ceil(pair/2)]

            return pair

        return [split_helper(pair[0]), split_helper(pair[1])]

    return split_helper(pair)


def add(pair_1, pair_2):
    pair = [pair_1, pair_2]

    while (explodable := can_explode(pair)) or (splittable := can_split(pair)):
        if explodable:
            pair = explode(pair)
        elif splittable:
            pair = split(pair)

    return pair


def find_magnitude(pair):
    if type(pair) == int:
        return pair

    return find_magnitude(pair[0]) * 3 + find_magnitude(pair[1]) * 2


def solve_part_1(pairs):
    n = len(pairs)
    pairs_sum = pairs[0]

    for i in range(1, n):
        pairs_sum = add(pairs_sum, pairs[i])

    return find_magnitude(pairs_sum)


def solve_part_2(pairs):
    res = 0
    n = len(pairs)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            res = max(res, find_magnitude(add(pairs[i], pairs[j])))

    return res


if __name__ == '__main__':
    with open('input_01.txt') as f:
        pairs = [json.loads(line) for line in f.readlines()]

        print(solve_part_1(pairs))
        print(solve_part_2(pairs))
