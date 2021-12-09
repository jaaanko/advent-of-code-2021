def get_sources(matrix):
    sources = []
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            up = down = left = right = float('inf')
            
            if i - 1 >= 0:
                up = matrix[i - 1][j]
            
            if i + 1 < m:
                down = matrix[i + 1][j]
            
            if j - 1 >= 0:
                left = matrix[i][j - 1]
            
            if j + 1 < n:
                right = matrix[i][j + 1]

            if matrix[i][j] < min(up, down, left, right):
                sources.append((i, j))

    return sources

def solve_part_1(matrix):
    res = 0
    sources = get_sources(matrix)

    for i, j in sources:
        res += matrix[i][j] + 1

    return res

def solve_part_2(matrix):
    sizes = []
    sources = get_sources(matrix)

    def dfs(i, j, prev):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 9 or (i, j) in visited or prev >= matrix[i][j]:
            return

        visited.add((i, j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for di,dj in directions:
            ni = i + di
            nj = j + dj

            dfs(ni, nj, matrix[i][j])
       
    for i, j in sources:
        visited = set()
        dfs(i, j, matrix[i][j] - 1)
        sizes.append(len(visited))
    
    res = 1

    for size in sorted(sizes, reverse = True)[:3]:
        res *= size
    
    return res

if __name__ == '__main__':
    with open('input_01.txt') as f:
        matrix =[]

        for line in f.readlines():
            matrix.append([int(x) for x in line.strip()])

        print(solve_part_1(matrix))
        print(solve_part_2(matrix))