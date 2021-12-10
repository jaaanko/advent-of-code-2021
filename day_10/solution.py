OPEN_TO_CLOSE = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>',
}

def get_first_illegal_closing(line):
    stack = []
    
    for char in line:
        if char in OPEN_TO_CLOSE:
            stack.append(char)
        else:
            if not stack or char != OPEN_TO_CLOSE[stack[-1]]:
                return char
            
            stack.pop()
    
    return None

def get_missing_closings(line):
    stack = []

    for char in line:
        if char in OPEN_TO_CLOSE:
            stack.append(char)
        else:            
            stack.pop()

    return [OPEN_TO_CLOSE[char] for char in stack][::-1]

def solve_part_1(lines):
    res = 0
    points = {
        ')' :  3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137, 
    }

    for line in lines:
        char = get_first_illegal_closing(line)

        if char is not None:
            res += points[char]

    return res

def solve_part_2(lines):
    res = []
    points = {
        ')' :  1,
        ']' : 2,
        '}' : 3,
        '>' : 4, 
    }

    incomplete_lines = [line for line in lines if get_first_illegal_closing(line) is None]

    for incomplete_line in incomplete_lines:
        missing = get_missing_closings(incomplete_line)
        curr = 0

        for char in missing:
            curr *= 5
            curr += points[char]

        res.append(curr)

    return sorted(res)[len(res) // 2]

if __name__ == '__main__':
    with open('input_01.txt') as f:
        lines = [line.strip() for line in f.readlines()]

        print(solve_part_1(lines))
        print(solve_part_2(lines))