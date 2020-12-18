import numpy as np

if __name__ == '__main__':

    # Part One
    def intervals_part_one(timestamp, buses):
        for i in range(0, timestamp+1):
            yield [ bus * i for bus in buses]

    def get_part_one():
        mins = [float("inf")] * len(buses)
        for i in intervals_part_one(timestamp, buses):

            mins = [t if (t > timestamp and t < mins[i.index(t)]) else mins[i.index(t)] for t in i ]
            filtered = [x for x in mins if x != float("inf")]

            if len(filtered) == len(buses):
                time = min(mins)
                minutes = time - timestamp
                busID =  buses[mins.index(time)]

                return minutes * busID

    # Part Two
    def get_part_two():
        
        timestamp = 0     
        step = buses[0]
        for bus in buses[1:]:
            while (timestamp + all_buses.index(bus)) % bus != 0:
                timestamp += step
            step *= bus
        
        return timestamp


               


    with open('./13/input.txt') as file:
        timestamp = int(file.readline())
        all_buses = file.readline().split(',')
        all_buses = [int(b) if b != "x" else b for b in all_buses ]
        buses = [int(b) for b in all_buses if b != "x"]


        

        #print(get_part_one())
        print(get_part_two())


