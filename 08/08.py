import copy

if __name__ == '__main__':


    def run_programm(instructions):
        i = 0
        acc = 0
        visited = []
        valid = True
        while i < len(instructions):
            
            if i in visited:
                valid = False
                break
            else:
                visited.append(i)
                if instructions[i][0] == "acc":
                    acc += int(instructions[i][1])
                if instructions[i][0] == "jmp":
                    i += int(instructions[i][1])
                    continue
            i += 1
        
        return acc, valid



    with open('./08/input.txt') as file:
        instructions = [x.split(" ") for x in file.read().splitlines()]
        print(run_programm(instructions))

        # just brute force part 2 idc
        switches = []
        for i, inst in enumerate(instructions):
            if inst[0] == "jmp" or inst[0] == "nop":
                switches.append(i)

        for switch in switches:
            new_instructions = copy.deepcopy(instructions)
            new_instructions[switch][0] = "nop" if new_instructions[switch][0] == "jmp" else "jmp"
            acc, valid = run_programm(new_instructions)
            if valid:
                print(acc)
                break