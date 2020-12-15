import copy
if __name__ == '__main__':

    def get_neighbors_part_one(y, x, _seats):
        neighs = []

        for y_speed in (-1, 0, 1):            
            for x_speed in (-1, 0, 1):
                    if y_speed == x_speed == 0: 
                        continue
                    else:
                        neighs.append(_seats[y + y_speed][x + x_speed])
        return neighs
                    
    
    def get_neighbors_part_two(y, x, _seats):
        neighs = []
        for y_speed in (-1, 0, 1):            
            for x_speed in (-1, 0, 1):
                if y_speed == x_speed == 0: 
                        continue
                _x = x + x_speed
                _y = y + y_speed
                while 0 <= _y < len(_seats) and 0 <= _x < len(_seats[0]):
                    if _seats[_y][_x] != '.':
                        neighs.append(_seats[_y][_x])
                        break
                    _x = _x + x_speed
                    _y = _y + y_speed
                    
        return neighs

    
    def permutate(before, seats, get_neighbours, thresshold):
        for y in range(1, len(seats)-1):
            for x in range(1, len(seats[0])-1):

                adjacents = get_neighbours(y, x, before)

                if seats[y][x] == 'L' and '#' not in adjacents:
                    seats[y][x] = '#'
                if seats[y][x] == '#' and adjacents.count('#') >= thresshold:
                    seats[y][x] = 'L'

    with open('./11/11.in') as file:
        seats = [['.'] + list(x) + ['.'] for x in file.read().splitlines()]
        seats.insert(0, ['.'] * len(seats[0]))
        seats.append(['.'] * len(seats[0]))
       
        before = []
        while before != seats:
            before = copy.deepcopy(seats)
            # Part One 
            #permutate(before, seats, get_neighbors_part_one, thresshold = 4)

            # Part Two
            permutate(before, seats, get_neighbors_part_two, thresshold = 5)

        print(sum(row.count('#') for row in seats))