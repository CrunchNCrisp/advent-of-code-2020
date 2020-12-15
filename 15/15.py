if __name__ == '__main__':

    with open('./15/15.in') as file:
        numbers = [int(x) for x in file.readline().split(",")]
        last_index = {}

        for i,n in enumerate(numbers):
            if i != len(numbers[:-1]):
                last_index[n] = i

        while len(numbers) < 30000000:
            last = numbers[-1]
            prev_last = last_index.get(last, -1)
            last_index[last] = len(numbers[:-1])
            if prev_last == -1:
                new_number = 0
            else:
                new_number = len(numbers[:-1]) - prev_last
            numbers.append(new_number)
            
            # Part One
            if len(numbers) == 2020:
                print(new_number)
        
        # Part Two
        print(numbers[-1])
