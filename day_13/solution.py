from copy import deepcopy

def count(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count = 0

    for i in range(m):
        for j in range(n):
            count += matrix[i][j] == '#'
    
    return count

def get_beautified_code(matrix, negative_space):
    code = ['\n']

    for row in matrix:
        line = ['\u2588' if char != negative_space else ' ' for char in row]
        line.append('\n')
        code.append(''.join(line))

    return ''.join(code)

def fold(matrix, direction, val):
    m1 = len(matrix)
    n1 = len(matrix[0])
    folded = None

    if direction == 'x':
        folded = []

        for i in range(m1):
            row = []
            for j in range(val):
                row.append(matrix[i][j])
            
            folded.append(row)
        
        matrix = [line[::-1] for line in matrix]
    else:
        folded = []

        for i in range(val):
            row = []
            for j in range(n1):
                row.append(matrix[i][j])
            
            folded.append(row)
                
        matrix = deepcopy(matrix)[::-1]

    m2 = len(folded)
    n2 = len(folded[0])

    for i in range(m2):
        for j in range(n2):
            folded[i][j] = '#' if matrix[i][j] == '#' else folded[i][j]     
    
    return folded

def solve_part_1(matrix, instructions):
    for x, y in points:  
        matrix[y][x] = '#'

    matrix = fold(matrix, instructions[0][0], instructions[0][1])
    return count(matrix)

def solve_part_2(matrix,instructions):
    for x, y in points:  
        matrix[y][x] = '#'
    
    for direction, val in instructions:
        matrix = fold(matrix, direction, val)

    return get_beautified_code(matrix, '.')

if __name__ == '__main__':
    with open('input_01.txt') as f:
        points = []
        instructions = []

        points_list, instructions_list = f.read().split('\n\n')

        for point in points_list.split('\n'):
            x, y = point.split(',')
            points.append((int(x), int(y)))

        for instruction in instructions_list.split('\n'):
            direction, val = instruction.split('=')
            instructions.append((direction[-1], int(val)))

        max_x = -1
        max_y = -1

        for x,y in points:
            max_x = max(max_x,x)
            max_y = max(max_y,y)
        
        matrix = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        print(solve_part_1(matrix, instructions))
        print(solve_part_2(matrix, instructions))