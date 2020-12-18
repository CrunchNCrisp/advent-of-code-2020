import re

if __name__ == '__main__':

       with open('./06/input.txt') as file:
        groups = [x for x in file.read().split("\n\n")]
        
        # Part One
        result = 0
        for group in groups:
            group_yes = set(group.replace("\n", ""))
            result += len(group_yes)
        print(result)

        # Part Two
        result = 0
        for group in groups:
            members = [set(x) for x in group.split("\n")]
            group_yes = members[0].intersection(*members)
            result += len(group_yes)
        print(result)