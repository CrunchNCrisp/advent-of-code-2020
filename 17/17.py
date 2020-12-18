import numpy as np
import collections
from pprint import pprint

with open('./17/input.txt') as file:
    lines = [x.strip() for x in file.read().splitlines()]

    # Part One
    space = np.array([list(cubes) for cubes in lines])
    space = space[:, :, np.newaxis]

    for _x in range(0, 6):
        space = np.pad(space, ((1, 1), (1, 1), (1, 1)), constant_values='.')
        new_space = np.copy(space)

        for x in range(space.shape[0]):
            for y in range(space.shape[1]):
                for z in range(space.shape[2]):
                    active_neighbors = 0
                    for _x in [-1, 0, 1]:
                        for _y in [-1, 0, 1]:
                            for _z in [-1, 0, 1]:
                                if _x == _y == _z == 0:
                                    continue
                                if 0 <= _x + x < space.shape[0] and 0 <= _y + y < space.shape[1] and 0 <= _z + z < space.shape[2]:
                                    if space[_x + x][_y + y][_z+z] == '#':
                                        active_neighbors += 1

                    previous = space[x][y][z]
                    new_space[x][y][z] = '.' if previous == '#' and active_neighbors not in [2, 3] else '#' if previous == '.' and active_neighbors == 3 else previous
        space = new_space
    print(np.sum(space == '#'))


    # Part Two
    space = np.array([list(cubes) for cubes in lines])
    space = space[:, :, np.newaxis, np.newaxis]
    for _x in range(0, 6):
        space = np.pad(space, ((1, 1), (1, 1), (1, 1), (1, 1)), constant_values='.')
        new_space = np.copy(space)
        for x in range(space.shape[0]):
            for y in range(space.shape[1]):
                for z in range(space.shape[2]):
                    for w in range(space.shape[3]):
                        active_neighbors = 0
                        for _x in [-1, 0, 1]:
                            for _y in [-1, 0, 1]:
                                for _z in [-1, 0, 1]:
                                    for _w in [-1, 0, 1]:
                                        if _x == 0 and _y == 0 and _z == 0 and _w == 0:
                                            continue
                                        if 0 <= _x + x < space.shape[0] and 0 <= _y + y < space.shape[1] and 0 <= _z + z < space.shape[2] and 0 <= _w + w < space.shape[3]:
                                            if space[_x + x][_y + y][_z + z][_w + w] == '#':
                                                active_neighbors += 1
                        previous = space[x][y][z][w]
                        new_space[x][y][z][w] = '.' if previous == '#' and active_neighbors not in [2, 3] else '#' if previous == '.' and active_neighbors == 3 else previous
        space = new_space
    print(np.sum(space == '#'))