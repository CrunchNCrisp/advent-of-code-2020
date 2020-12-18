import re

if __name__ == '__main__':

    def binary_search(input_string, seat_list):
        # end of recursion
        if len(seat_list) == 1:
            return seat_list[0]

        # first half
        elif input_string[0] == "0":
            y = round(len(seat_list)/2)
            return binary_search(input_string[1:], seat_list[:y])
        
        # second half
        elif input_string[0] == "1":
            y = round(len(seat_list)/2)
            return binary_search(input_string[1:], seat_list[y:])


    def get_seat_id(boarding_pass, n_rows = 128, n_cols = 8):
        seat_list = list(range(0,  n_rows))
        row = binary_search(boarding_pass[:7], seat_list)

        seat_list = list(range(0,  n_cols))
        col = binary_search(boarding_pass[7:], seat_list)
        return (row * 8) + col

    with open('./05/input.txt') as file:
        entries = [x.replace("L","0").replace("R","1").replace("F","0").replace("B","1") for x in file.read().splitlines()]
        seat_ids = [get_seat_id(x) for x in entries]
        print(max(seat_ids))
        seat_next_to_me = list(filter(lambda x: ((x-1 not in seat_ids) and (x-2 in seat_ids)), seat_ids))
        print(seat_next_to_me[0] - 1)