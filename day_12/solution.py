from collections import defaultdict

START = 'start'
END = 'end'

def is_small_cave(tile):
    return tile not in (START, END) and tile.islower()

def solve_part_1(adj):
    visited = set()

    def dfs(curr_tile):
        if curr_tile == END:
            return 1

        if is_small_cave(curr_tile):
            visited.add(curr_tile)

        paths = 0

        for nxt in adj[curr_tile]:
            if nxt in visited or nxt == START:
                continue

            paths += dfs(nxt)

        if curr_tile in visited:
            visited.remove(curr_tile)

        return paths

    return dfs(START)

def solve_part_2(adj):
    visited = defaultdict(int)
    small_caves = [tile for tile in adj if is_small_cave(tile)]

    def dfs(curr_tile, extra):
        if curr_tile == END:
            return 1

        if curr_tile == START:
            if visited[START] > 0:
                return 0
            
            visited[START] += 1

        if is_small_cave(curr_tile):
            if visited[curr_tile] >= 2 or visited[curr_tile] == 1 and curr_tile != extra:
                return 0

            visited[curr_tile] += 1

        paths = 0

        for neigh in adj[curr_tile]:
            paths += dfs(neigh, extra)

        if is_small_cave(curr_tile):
            visited[curr_tile] -= 1

        return paths
    
    res = 0

    for cave in small_caves:
        res += dfs(START, cave)
        visited = defaultdict(int)

    res -= solve_part_1(adj) * (len(small_caves) - 1)

    return res

if __name__ == '__main__':
    with open('input_01.txt') as f:
        edges = []

        for line in f.readlines():
            line = line.strip()
            edges.append(line.split('-'))

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        print(solve_part_1(adj))
        print(solve_part_2(adj))