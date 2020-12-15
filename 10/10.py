if __name__ == '__main__':

    with open('./10/10.in') as file:
        adapters = [int(x) for x in file.read().splitlines()]
        adapters.append(0)
        adapters.sort()
        device_adapter = adapters[-1] + 3
        adapters.append(device_adapter)
        
        # Part One
        ones = 0
        threes = 0
        for i in range(len(adapters)-1):
            if adapters[i+1] - adapters[i] == 1:
                ones += 1
            elif adapters[i+1] - adapters[i] == 3:
                threes  += 1
        print(ones, threes, ones*threes)
        
        # Part Two
        def find_path(start, end, cache):
            count = 0

            if start == end:
                return 1
            if start in cache:
                return cache[start]
            else:
                neighbors = [x for x in adapters[adapters.index(start)+1 : adapters.index(start) + 4] if x - start <= 3]
                for neighbor in neighbors :
                        count += find_path(neighbor, end, cache)
            cache[start] = count 
            return count

        n = find_path(adapters[0], device_adapter, {})
        print(n)
