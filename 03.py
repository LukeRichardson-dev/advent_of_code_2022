TEST = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


def p1(inp):

    rucksacks = inp.split('\n')
    score = 0
    for rs in rucksacks:
        mid = len(rs) // 2
        l, r = rs[:mid], rs[mid:]

        lset = set(l)
        rset = set(r)

        diff = lset.intersection(rset).pop()
        score += convert(diff)

    return score

def p2(inp):

    rucksacks = inp.split('\n')
    groups = zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])
    score = 0
    for a, b, c in groups:
        aset = set(a)
        bset = set(b)
        cset = set(c)

        res = aset.intersection(bset).intersection(cset)
        score += convert(res.pop())

    return score

def convert(ch):

    o = ord(ch)
    if 65 <= o < 91:
        return o - 38

    return o - ord('a') + 1

if __name__ == '__main__':

    # print(convert('a'))
    # print(convert('z'))
    # print(convert('A'))
    # print(convert('Z'))

    with open('03.txt') as f:

        inp = f.read()

    res = p2(inp)
    print(res)