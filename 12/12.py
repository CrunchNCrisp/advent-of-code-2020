from enum import Enum
if __name__ == '__main__':

    def move(d, v):
        if d == 0   : return 0,        (1 * v)
        if d == 90  : return (1 * v),  0
        if d == 180 : return 0,        (-1 * v)
        if d == 270 : return (-1 * v), 0
    
    def rotate(pd, a, x, y):
        if a == 0:
            return x,y
        if a == 90:
            return y,-x
        if a == 180:
            return -x, -y
        if a == 270:
            return -y, x


    with open('./12/12.in') as file:
        directions = [ (x[0], int(x[1:])) for x in file.read().splitlines()]
        ds = {
            "N" : 0,
            "E" : 90,
            "S" : 180,
            "W" : 270,
        }

        # Part One
        x = 0
        y = 0
        cd = 90

        for dirs in directions:
            d = dirs[0]
            v = dirs[1]

            if d == 'L':
                cd = (cd - v) % 360
                continue
            elif d == 'R':
                cd = (cd + v) % 360
                continue
            elif d != 'F':
                cd = ds[d]
                
            _x, _y = move(cd, v)
            x += _x
            y += _y
        
        print(x, y, abs(x)+abs(y))


        # Part Two
        x_ship = 0
        y_ship = 0
        
        x_wp = 10
        y_wp = 1

        cd = 90

        for dirs in directions:
            d = dirs[0]
            v = dirs[1]
            print(d, v)


            if d == 'R':
                x_wp, y_wp = rotate(cd, v, x_wp, y_wp)                
            elif d == 'L':
                x_wp, y_wp = rotate(cd, 360-v, x_wp, y_wp)
            elif d == 'F':
                # Move Ship 
                x_ship += x_wp * v
                y_ship += y_wp * v

            else:
                # Only Move Waypoint
                cd = ds[d]
                _x, _y = move(cd, v)
                x_wp += _x
                y_wp += _y

        print(abs(x_ship)+abs(y_ship))