from collections import defaultdict

def count_overlaps(points):
    overlaps = 0
    
    for x, y in points:
        if points[x, y] > 1:
            overlaps += 1
    
    return overlaps

def solve_part_1(lines):
    points = defaultdict(int)

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1,y2) + 1):
                points[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[x, y1] += 1

    return count_overlaps(points)

def solve_part_2(lines):
    points = defaultdict(int)

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1,y2) + 1):
                points[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[x, y1] += 1
        else:
            dx = -1 if x1 > x2 else 1
            dy = -1 if y1 > y2 else 1

            while x1 != x2:
                points[x1, y1] += 1
                x1 += dx
                y1 += dy
            
            points[x1, y1] += 1

    return count_overlaps(points)

if __name__ == '__main__':
    with open('input_01.txt') as f:
        lines = []

        for line in f.readlines():
            segment = line.strip().split(' -> ')

            coords1 = [int(n) for n in segment[0].split(',')]
            coords2 = [int(n) for n in segment[1].split(',')]

            lines.append([coords1,coords2])

        print(solve_part_1(lines))
        print(solve_part_2(lines))