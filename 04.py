def p1(inp):
    count = 0

    for line in inp.split('\n'):

        ra, rb = line.split(',')
        sa, sb = range_to_set(ra), range_to_set(rb)

        if sa.issubset(sb) or sb.issubset(sa):
            count += 1
    
    return count

def p2(inp):
    count = 0

    for line in inp.split('\n'):

        ra, rb = line.split(',')
        sa, sb = range_to_set(ra), range_to_set(rb)

        if len(sb.intersection(sa)):
            count += 1
    
    return count

def range_to_set(rs):

    ra, rb = rs.split('-')
    a, b = int(ra), int(rb)
    return set(range(a, b+1))


TEST = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

if __name__ == '__main__':

    with open('04.txt') as f:
        inp = f.read()

    res = p2(inp)

    print(res)