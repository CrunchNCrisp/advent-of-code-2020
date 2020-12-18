import re
import copy

if __name__ == '__main__':

    def apply_mask(value, mask):
        value |= int(mask.replace('X', '0'), 2)
        value &= int(mask.replace('X', '1'), 2)
        return value

    def generate_addresses(address):
        if 'X' not in address:
            yield int(address, 2)
        else:
            yield from generate_addresses(address.replace('X', '1', 1))
            yield from generate_addresses(address.replace('X', '0', 1))

    with open('./14/input.txt') as file:
        instructions = [x.split(" = ") for x in file.read().splitlines()]
        
        current_mask = []
        memory = {}
        for i in instructions:
            
            if i[0] == "mask":
                current_mask = i[1]
            else:
                address = re.findall(r'\d+', i[0])[0]

                # Part One
                # memory[address] = apply_mask(int(i[1]), current_mask)

                # Part Two
                padded_address_binary = str(bin(int(address)))[2:].rjust(36, '0')
                permutation_candidates = ""

                # should probably do list comprehesnion
                for og, mask_value in zip(padded_address_binary, current_mask):
                    if mask_value == "0": permutation_candidates += og
                    if mask_value == "X": permutation_candidates += mask_value
                    if mask_value == "1": permutation_candidates += mask_value
                
                #print(padded_address_binary)
                #print(current_mask)
                #print(permutation_candidates)

                for addr in generate_addresses(permutation_candidates):
                    memory[addr] = int(i[1])

        print(sum(memory.values()))


