if __name__ == '__main__':

    with open('./14/14.in') as file:
        instructions = [x.split(" = ") for x in file.read().splitlines()]