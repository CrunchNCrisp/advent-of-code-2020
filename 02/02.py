if __name__ == '__main__':

    def is_correct_part_one(min, max, c,  string):
        count = 0
        for _ in string:
            if _ == c:
                count +=1

        return count >= min and count <= max
    
    def is_correct_part_two(pos1, pos2, c,  string):
        return (string[pos1-1] == c) != (string[pos2-1] == c)

    def get_count(entries, is_correct):
        entries = [1 for x in entries if is_correct(int(x[0]),int(x[1]),x[2],x[3])]
        return len(entries)

    with open('./02/02-input.txt') as file:
        entries = [x.replace(':', '').replace('-', " ").split() for x in file.read().splitlines()]
        print(get_count(entries, is_correct_part_one))
        print(get_count(entries, is_correct_part_two))