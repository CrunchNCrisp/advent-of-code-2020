if __name__ == '__main__':

    def find_pair(entries, goalsum):
        for n1 in entries:
            for n2 in entries:
                if n1 + n2 == goalsum and n1 != n2:
                    return (n1,n2)
        return (-1,-1)

    def find_defect(numbers, len_preamble):
            defect = None
            for n in range(len_preamble, len(numbers)):
                preamble = numbers[(n - len_preamble):n]
                if find_pair(preamble, numbers[n]) == (-1,-1):
                     defect = numbers[n]
            return defect
            
    def find_contingency(numbers, defect):
        for idx in enumerate(numbers):
            c = []
            i = idx[0]
            found = False

            while True:
                if sum(c) == defect and len(c) > 1:
                    found = True
                    break
                elif sum(c) > defect:
                    found = False
                    break
                elif sum(c) < defect:
                    c.append(numbers[i])
                    i += 1
            
            if found:
                return max(c) + min(c)

        return -1



    with open('./09/input.txt') as file:
        numbers = [int(x) for x in file.read().splitlines()]

        x = find_defect(numbers, 25)
        print(find_contingency(numbers, x))

            