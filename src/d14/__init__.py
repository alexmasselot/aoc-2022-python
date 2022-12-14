from itertools import chain

from utils import read_input


def read_path(text: str):
    bs = [b.split(',') for b in text.split(' -> ')]
    return [(int(b[0]), int(b[1])) for b in bs]


def path_points(path):
    def b_range(s, e):
        return range(s, e + 1) if s < e else range(e, s + 1)

    p1 = path[0]
    points = set()
    for ip, p2 in enumerate(path[1:]):
        for i in b_range(p1[0], p2[0]):
            for j in b_range(p1[1], p2[1]):
                points.add((i, j))
        p1 = p2
    return points


def print_world(world, x_min):
    for l in world:
        print(''.join(l[(x_min - 1):]))


def drop_sand(world, y_max):
    (i, j) = 500, 0
    move = True
    while move and j < y_max:
        j = j + 1

        if world[j][i] == '.':
            pass
        elif world[j][i - 1] == '.':
            i = i - 1
        elif world[j][i + 1] == '.':
            i = i + 1
        else:
            world[j - 1][i] = 'o'
            move = False
    return not (move or (j == 1) or j > y_max)


def drop_sand_part_2(world, y_max):
    (i, j) = 500, 0
    move = True
    while move and (world[1][499] == '.' or world[1][500] == '.' or world[1][501] == '.'):
        j = j + 1
        if j == y_max + 2:
            world[j - 1][i] = 'o'
            move = False
        elif world[j][i] == '.':
            pass
        elif world[j][i - 1] == '.':
            i = i - 1
        elif world[j][i + 1] == '.':
            i = i + 1
        else:
            world[j - 1][i] = 'o'
            move = False
    return world[1][499] == '.' or world[1][500] == '.' or world[1][501] == '.'


if __name__ == '__main__':
    lines = read_input('input-a.txt')

    paths = [read_path(l) for l in lines]
    y_max = max([p[1] for p in list(chain(*paths))]) + 3
    x_min = min([p[0] for p in list(chain(*paths))])
    x_min = min([x_min, 500 - y_max - 4])
    x_max = max([p[0] for p in list(chain(*paths))])
    x_max = max([x_max, 500 + y_max + 4])

    world = [
        list('.' * (x_max + 2)) for i in range(0, y_max + 1)
    ]

    is_part_2 = True
    if is_part_2:
        paths.append([(x_min - 1, y_max - 1), (x_max + 1, y_max - 1)])

    for path in paths:
        for p in path_points(path):
            world[p[1]][p[0]] = '#'

    n = 0
    while drop_sand(world, y_max):
        n += 1

    print_world(world, x_min)
    if is_part_2:
        print(n + 1)
    else:
        print(n)
