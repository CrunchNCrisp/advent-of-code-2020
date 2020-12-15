if __name__ == '__main__':

    def find_pair(entries, sum = 2020):
        for entry in entries:
            key = sum - entry
            if key in entries:
                return(key, entry)
        return (-1,-1)

    def find_triplet(entries, sum = 2020):
        for entry in entries:
            key = sum-entry
            k,v = find_pair(entries, sum=key)

            if (k,v) != (-1,-1):
                return k,v,entry
        return(-1,-1,-1)

    with open('./01/01-input.txt') as file:
        entries = set([int(x) for x in file.read().splitlines()])
        
        k,v = find_pair(entries)
        print(k, v, k*v)

        k,v,n = find_triplet(entries)
        print(k,v,n, k*v*n)