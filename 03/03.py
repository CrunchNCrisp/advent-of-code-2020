if __name__ == '__main__':

    def get_tree_count(course, x = 0, x_speed = 3, y_speed = 1):
        
        width = len(course[0])
        length = len(course)
        count = 0

        for y in range(0, length, y_speed):
            if course[y][x] == '#':
                count += 1
            x = (x + x_speed) % width

        return count

    with open('./03/03-input.txt') as file:
        lines = [x for x in file.read().splitlines()]

        slopes = [(3,1), (1,1), (5,1), (7,1), (1,2)]
        result = 1
        for slope in slopes:
            result *= get_tree_count(lines, x_speed=slope[0], y_speed=slope[1]) 
        print(result)
