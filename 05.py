
IV = '''QFLSR
TPGQZN
BQMS
QBCHJZGT
SFNBMHP
GVLSNQCP
FCW
MPVWZGHQ
RNCLDZG'''

TIV = '''NZ
DCM
P'''

TEST = '''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

def parse_instr(instr):

    _, ra, _, rb, _, rc = instr.split(' ')
    return int(ra), int(rb) - 1, int(rc) - 1

def p1(iv, inst):

    ivs = [list(i[::-1]) for i in iv.split('\n')]
    for a, b, c in map(parse_instr, inst.split('\n')):
        
        for _ in range(a):

            ivs[c].append(ivs[b].pop())

    return ivs

def p2(iv, inst):

    ivs = [list(i[::-1]) for i in iv.split('\n')]
    for a, b, c in map(parse_instr, inst.split('\n')):
        
        buffer = []
        for _ in range(a):

            buffer.append(ivs[b].pop())

        for i in buffer[::-1]:
            ivs[c].append(i)

    return ivs


if __name__ == '__main__':

    with open('05.txt') as f:

        text = f.read()

    res = p2(IV, text)
    print(''.join((str(i[-1]) for i in res)))
    