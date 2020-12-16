if __name__ == '__main__':

    with open('./15/15.in') as file:
        numbers = [int(x) for x in file.readline().split(",")]
        last_index = {}

        for i,n in enumerate(numbers):
            if i != len(numbers[:-1]):
                last_index[n] = i

        i = len(numbers)
        n = numbers[-1]
        while i < 30000000:
            prev_last = last_index.get(n, -1)
            last_index[n] = i - 1
            if prev_last == -1:
                new_number = 0
            else:
                new_number = i - 1 - prev_last
            n = new_number
            i += 1
            # Part One
            if i == 2020:
                print(n)

            
        # Part Two
        print(n)
