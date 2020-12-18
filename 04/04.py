import re

if __name__ == '__main__':

    def line_to_dict(line):
        d = {}
        for l in line.strip().split(" "):
            l = l.split(":")
            d[l[0]] = l[1]
        return d

    def are_present(entry):
        fields = [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid',
        ]

        c = list(filter(lambda x: x not in entry,  fields))
        return len(c) == 0

    def are_valid(entry):
        byr = re.fullmatch(r'(19[2-9]\d|200[0-2])', entry['byr'])
        iyr = re.fullmatch(r'(201\d|2020)', entry['iyr'])
        eyr = re.fullmatch(r'(202\d|2030)', entry['eyr'])
        hgt = re.fullmatch(r'((1[5-8]\d|19[0-3])cm)|((59|6\d|7[0-6])in)', entry['hgt'])
        hcl = re.fullmatch(r'#[0-9a-f]{6}', entry['hcl'])
        ecl = re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', entry['ecl'])
        pid = re.fullmatch(r'\d{9}', entry['pid'])
        return all((byr, iyr, eyr, hgt, hcl, ecl, pid))
        
    with open('./04/input.txt') as file:
        entries = [line_to_dict(x.replace("\n", " ")) for x in file.read().split("\n\n")]

        count = 0
        for entry in entries:
            if are_present(entry) and are_valid(entry): count += 1
        print(count)