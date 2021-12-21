from functools import cache


def find_new_pos(curr_pos, moves):
    return (curr_pos + moves - 1) % 10 + 1


def solve_part_1(pos_1, pos_2):
    score_1 = score_2 = total_rolls = curr_roll = 0

    while score_1 < 1000 and score_2 < 1000:
        move_1 = move_2 = 0

        for _ in range(3):
            curr_roll = 1 if curr_roll + 1 > 100 else curr_roll + 1
            move_1 += curr_roll
            total_rolls += 1

        pos_1 = find_new_pos(pos_1, move_1)
        score_1 += pos_1

        if score_1 >= 1000:
            break

        for _ in range(3):
            curr_roll = 1 if curr_roll + 1 > 100 else curr_roll + 1
            move_2 += curr_roll
            total_rolls += 1

        pos_2 = find_new_pos(pos_2, move_2)
        score_2 += pos_2

    return min(score_1, score_2) * total_rolls


@cache
def count_player_1_wins(score_1, score_2, pos_1, pos_2, rolls, player_1_turn):
    if score_1 >= 21:
        return 1

    if score_2 >= 21:
        return 0

    res = 0

    if player_1_turn:
        if rolls > 0:
            for roll in range(1, 4):
                res += count_player_1_wins(score_1, score_2,
                                           find_new_pos(pos_1, roll), pos_2, rolls - 1, True)
        else:
            res += count_player_1_wins(score_1 + pos_1,
                                       score_2, pos_1, pos_2, 3, False)

    else:
        if rolls > 0:
            for roll in range(1, 4):
                res += count_player_1_wins(score_1, score_2, pos_1,
                                           find_new_pos(pos_2, roll), rolls - 1, False)
        else:
            res += count_player_1_wins(score_1,
                                       score_2 + pos_2, pos_1, pos_2, 3, True)

    return res


def solve_part_2(pos_1, pos_2):
    return max(count_player_1_wins(0, 0, pos_1, pos_2, 3, True), count_player_1_wins(0, 0, pos_2, pos_1, 3, False))


if __name__ == '__main__':
    with open('input_01.txt') as f:
        line_1, line_2 = f.read().split('\n')

        pos_1 = int(line_1.split(': ')[1])
        pos_2 = int(line_2.split(': ')[1])

        print(solve_part_1(pos_1, pos_2))
        print(solve_part_2(pos_1, pos_2))
