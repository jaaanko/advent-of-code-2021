from collections import namedtuple

Area = namedtuple('Area', ['lower_x', 'upper_x', 'lower_y', 'upper_y'])


def can_visit_target(x_velocity, y_velocity, target):
    x = y = 0

    while x <= target.upper_x and y >= target.lower_y:
        if target.lower_x <= x <= target.upper_x and target.lower_y <= y <= target.upper_y:
            return True

        x += x_velocity
        y += y_velocity
        y_velocity -= 1
        x_velocity = max(0, x_velocity - 1)

    return False


def get_min_x_velocity(lower_x, upper_x):
    for i in range(upper_x+1):
        if lower_x <= i * (i + 1) // 2 <= upper_x:
            return i

    return -1


def solve_part_1(target):
    min_x_velocity = get_min_x_velocity(target.lower_x, target.upper_x)
    max_y_velocity = 0

    for y_velocity in range(target.lower_y, abs(target.lower_y)):
        if can_visit_target(min_x_velocity, y_velocity, target):
            max_y_velocity = max(max_y_velocity, y_velocity)

    return max_y_velocity * (max_y_velocity + 1) // 2


def solve_part_2(target):
    min_x_velocity = get_min_x_velocity(target.lower_x, target.upper_x)
    count = 0

    for x in range(min_x_velocity, target.upper_x + 1):
        for y in range(target.lower_y, abs(target.lower_y)):
            count += can_visit_target(x, y, target)

    return count


if __name__ == '__main__':
    with open('input_01.txt') as f:
        coords = f.readline().strip().split(': ')[1]
        x_coords, y_coords = coords.split(', ')

        lower_x, upper_x = x_coords.split('..')
        lower_x, upper_x = int(lower_x[2:]), int(upper_x)

        lower_y, upper_y = y_coords.split('..')
        lower_y, upper_y = int(lower_y[2:]), int(upper_y)

        target = Area(lower_x, upper_x, lower_y, upper_y)

        print(solve_part_1(target))
        print(solve_part_2(target))
