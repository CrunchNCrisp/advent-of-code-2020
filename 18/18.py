import re

class aoc_int(int):
    def __pow__(self, other):
        return aoc_int(int(self) + other)
    def __sub__(self, other):
        return aoc_int(int(self) * other)
    def __mul__(self, other):
        return aoc_int(int(self) * other)
    def __add__(self, other):
        return aoc_int(int(self) + other)


def evaluate(expression, part_two=False):
    expression = re.sub(r"(\d+)", r"aoc_int(\1)", expression)
    expression = expression = expression.replace("+", "**") if part_two else expression.replace("*", "-") 
    return eval(expression, {}, {"aoc_int": aoc_int})


with open('./18/input.txt') as file:
    lines = [x.strip() for x in file.read().splitlines()]

    # Part One
    print(sum(evaluate(line) for line in lines))
    
    # Part Two
    print(sum(evaluate(line, part_two=True) for line in lines))