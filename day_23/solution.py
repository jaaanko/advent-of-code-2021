from functools import cache

COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}


def hallway_passable(hallway, curr_tile, next_tile):
    mn = min(curr_tile, next_tile)
    mx = max(curr_tile, next_tile)

    if mn == curr_tile:
        mn += 1

    if mx == curr_tile:
        mx -= 1

    for i in range(mn, mx+1):
        if hallway[i] != '.':
            return False

    return True


def room_passable(room, start):
    for i in range(start-1, -1, -1):
        if room[i].isalpha():
            return False

        if room[i].isdigit():
            break

    return True


def room_complete(rooms, j, mapping):
    for i in range(j+1, len(rooms)):
        if rooms[i] == ',':
            break

        if rooms[i] != mapping[j]:
            return False

    return True


def room_empty(rooms, j):
    for i in range(j+1, len(rooms)):
        if rooms[i] == ',':
            break

        if rooms[i] != '.':
            return False

    return True


def room_partially_complete(rooms, j, mapping):
    last = -1
    found = False

    for i in range(j+1, len(rooms)):
        if rooms[i] == ',':
            last = i
            break

    for i in range(last-1, j, -1):
        if rooms[i] == '.':
            break
        elif rooms[i] != mapping[j]:
            return False
        else:
            found = True

    return found


def get_last_available_spot(rooms, j):
    last = -1

    for i in range(j+1, len(rooms)):
        if rooms[i] == ',':
            last = i
            break

    for i in range(last-1, j, -1):
        if rooms[i] == '.':
            return i - j

    return -1


def solve_part_1(grid):
    valid_tiles = [0, 1, 3, 5, 7, 9, 10]
    j = 3
    rooms = []

    room_num_to_letter = {
        0: 'A',
        4: 'B',
        8: 'C',
        12: 'D',
    }

    letter_to_room_num = {
        'A': 0,
        'B': 4,
        'C': 8,
        'D': 12,
    }

    for i in range(2, 10, 2):
        rooms.append(str(i) + grid[2][j] + grid[3][j] + ',')
        j += 2

    rooms = ''.join(rooms)
    best = float('inf')

    @cache
    def min_total_energy(hallway, rooms, energy_spent):
        nonlocal best

        if energy_spent > best or all(room_complete(rooms, i, room_num_to_letter) for i in range(0, 13, 4)):
            return energy_spent

        res = float('inf')

        for i in range(0, len(rooms), 4):
            if room_empty(rooms, i) or room_complete(rooms, i, room_num_to_letter) or room_partially_complete(rooms, i, room_num_to_letter):
                continue

            for j in range(1, 3):
                letter = rooms[i+j]

                if letter == '.' or not room_passable(rooms, i+j):
                    continue

                curr_tile = int(rooms[i])
                cost = COSTS[letter] * j

                for next_tile in valid_tiles:
                    if not hallway_passable(hallway, curr_tile, next_tile):
                        continue

                    new_hallway = hallway[:next_tile] + \
                        letter + hallway[next_tile+1:]
                    new_rooms = rooms[:i+j] + '.' + rooms[i+j+1:]

                    res = min(res, min_total_energy(
                        new_hallway, new_rooms, energy_spent + cost + COSTS[letter] * (abs(curr_tile-next_tile))))

                    best = min(best, res)

        for i in range(len(hallway)):
            if hallway[i] == '.':
                continue

            letter = hallway[i]
            room_index = letter_to_room_num[letter]

            if not hallway_passable(hallway, i, int(rooms[room_index])):
                continue

            if room_empty(rooms, room_index) or room_partially_complete(rooms, room_index, room_num_to_letter):
                new_hallway = hallway[:i] + '.' + hallway[i+1:]
                inserted_index = get_last_available_spot(
                    rooms, room_index)

                cost = (COSTS[letter] * (abs(int(rooms[room_index]) - i))
                        ) + (COSTS[letter] * (inserted_index))

                new_rooms = rooms[:room_index+inserted_index] + \
                    letter + rooms[room_index+inserted_index+1:]

                res = min(res, min_total_energy(
                    new_hallway, new_rooms, energy_spent + cost))

                best = min(best, res)

        return res

    return min_total_energy('.' * 11, rooms, 0)


def solve_part_2(grid):
    valid_tiles = [0, 1, 3, 5, 7, 9, 10]
    grid = grid[:3] + ['  #D#C#B#A#  ', '  #D#B#A#C#  '] + grid[3:]
    j = 3
    rooms = []

    for i in range(2, 10, 2):
        rooms.append(str(i) + ''.join(grid[k][j] for k in range(2, 6)) + ',')
        j += 2

    rooms = ''.join(rooms)
    best = float('inf')

    room_num_to_letter = {
        0: 'A',
        6: 'B',
        12: 'C',
        18: 'D',
    }

    letter_to_room_num = {
        'A': 0,
        'B': 6,
        'C': 12,
        'D': 18,
    }

    # function can be generalized for both parts.
    @cache
    def min_total_energy(hallway, rooms, energy_spent):
        nonlocal best

        if energy_spent > best or all(room_complete(rooms, i, room_num_to_letter) for i in range(0, 19, 6)):
            return energy_spent

        res = float('inf')

        for i in range(0, len(rooms), 6):
            if room_empty(rooms, i) or room_complete(rooms, i, room_num_to_letter) or room_partially_complete(rooms, i, room_num_to_letter):
                continue

            for j in range(1, 5):
                letter = rooms[i+j]

                if letter == '.' or not room_passable(rooms, i+j):
                    continue

                curr_tile = int(rooms[i])
                cost = COSTS[letter] * j

                for next_tile in valid_tiles:
                    if not hallway_passable(hallway, curr_tile, next_tile):
                        continue

                    new_hallway = hallway[:next_tile] + \
                        letter + hallway[next_tile+1:]
                    new_rooms = rooms[:i+j] + '.' + rooms[i+j+1:]

                    res = min(res, min_total_energy(
                        new_hallway, new_rooms, energy_spent + cost + COSTS[letter] * (abs(curr_tile-next_tile))))

                    best = min(best, res)

        for i in range(len(hallway)):
            if hallway[i] == '.':
                continue

            letter = hallway[i]
            room_index = letter_to_room_num[letter]

            if not hallway_passable(hallway, i, int(rooms[room_index])):
                continue

            if room_empty(rooms, room_index) or room_partially_complete(rooms, room_index, room_num_to_letter):
                new_hallway = hallway[:i] + '.' + hallway[i+1:]
                inserted_index = get_last_available_spot(
                    rooms, room_index)

                cost = (COSTS[letter] * (abs(int(rooms[room_index]) - i))
                        ) + (COSTS[letter] * (inserted_index))

                new_rooms = rooms[:room_index+inserted_index] + \
                    letter + rooms[room_index+inserted_index+1:]

                res = min(res, min_total_energy(
                    new_hallway, new_rooms, energy_spent + cost))

                best = min(best, res)

        return res

    return min_total_energy('.' * 11, rooms, 0)


if __name__ == '__main__':
    with open('input_01.txt') as f:
        grid = [line.strip() for line in f.readlines()]

        for i in range(3, len(grid)):
            grid[i] = '  ' + grid[i] + '  '

        print(solve_part_1(grid))
        print(solve_part_2(grid))
