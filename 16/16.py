import re
from collections import defaultdict
from itertools import chain

with open('./16/input.txt') as file:
    lines = [x for x in file.read().splitlines()]
    
    field_ranges = defaultdict(list)
    # read in ranges and fields
    for line in lines:
        if line == "":
            break
        else:
            field_name, ranges = line.split(": ")
            ranges = ranges.split(" or ")
            for r in ranges:
                lb, ub = map(int, r.split("-"))
                field_ranges[field_name].append(list(range(lb, ub+1)))

    # read in tickets
    my_ticket = list(map(int, lines[lines.index('your ticket:')+1].split(",")))
    nearby_tickets = [list(map(int, (line.split(",")))) for line in lines[lines.index('nearby tickets:')+1:]]

    # Part One
    all_values = set(chain.from_iterable(list(chain.from_iterable(field_ranges.values()))))
    all_ticket_values = list(chain.from_iterable(nearby_tickets))
    invalid = [x for x in all_ticket_values if x not in all_values]
    print(sum(invalid))

    # Part Two
    cleaned_nearby_tickets = [ticket for ticket in nearby_tickets if not any(value in invalid for value in ticket)]
    same_field = list(zip(*cleaned_nearby_tickets))

    possible = defaultdict(list)
    for i, sf in enumerate(same_field):
        for field, r in field_ranges.items():
            field_values = list(chain.from_iterable(r))
            if all(value in field_values for value in sf):
                possible[i].append(field)
    
    while any(len(p) > 1 for p in possible.values()):
        to_pop = list(chain.from_iterable([v for v in possible.values() if len(v) == 1]))
        possible = { k: values if len(values) == 1 else list(set(values)- set(to_pop)) for k,values in possible.items() }

    result = 1
    for i, field in possible.items():
        if field[0].startswith("departure"):
            result *= my_ticket[i]
    print(result)


  