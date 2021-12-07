def solve_part_1(positions):
    res = float('inf')

    for i in range(min(positions), max(positions) + 1):
        curr = 0

        for num in positions:
            curr += abs(num - i)
        
        res = min(res, curr)

    return res

def solve_part_2(positions):
    res = float('inf')

    for i in range(min(positions), max(positions) + 1):
        curr = 0

        for pos in positions:
            n = abs(pos - i)
            curr += n * (n + 1) // 2
        
        res = min(res, curr)

    return res

if __name__ == '__main__':
    with open('input_01.txt') as f:
        positions = [int(x) for x in f.readline().split(',')]

        print(solve_part_1(positions))
        print(solve_part_2(positions))