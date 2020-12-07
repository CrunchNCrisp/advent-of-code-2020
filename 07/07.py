import collections

if __name__ == '__main__':


    with open('./07/07.in') as file:
        bag_list = [x for x in file.read().splitlines()]

        color_contains = collections.defaultdict(list)
        color_contained_in = collections.defaultdict(set)
        
        for bag in bag_list:
            bag_color  = bag.split(" bags contain ")[0]
            bag_content = bag.split(" bags contain ")[1].split(", ")

            for content in bag_content:
                amount = content.split(" ", 1)[0]
                if amount == "no":
                    amount = 0
                else:
                    amount = int(amount)
                color = content.split(" ", 1)[1].split(" bag")[0]

                color_contains[bag_color].append((amount, color))
                color_contained_in[color].add(bag_color)
        

        # Part One
        def check_for_colors(color):
            gold_bags = set()
            for bag_color in color_contained_in[color]:
                gold_bags.add(bag_color)
                gold_bags |= check_for_colors(bag_color)
            return gold_bags
        print(len(check_for_colors("shiny gold")))

        # Part Two
        color_amount = {}
        def check_for_amount(color):
            total = 0
            for a, c in color_contains[color]:
                total += a
                if color in color_amount.keys():
                    total += a * color_amount[color]
                else:
                    total += a * check_for_amount(c)
            color_amount[color] = total
            return total
        
        print(check_for_amount("shiny gold"))
