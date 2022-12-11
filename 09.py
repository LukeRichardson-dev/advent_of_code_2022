def p1(inp: str):
    h = (0, 0)
    t  = (0, 0)

    ts = set()
    
    for i in inp.split('\n'):

        d, rm = i.split(' ')
        r = int(rm)

        if d == 'R':
            dxy = (1, 0)
        elif d == 'L':
            dxy = (-1, 0)
        elif d == 'U':
            dxy = (0, 1)
        else:
            dxy = (0, -1)

        for _ in range(r):
            h, t = move(h, t, dxy)
            ts.add(t)

        print(h, t)

    return ts

def p2(inp: str):
    rope = [(0, 0)] * 10
    ts = set([(0, 0)])
    
    for i in inp.split('\n'):

        d, rm = i.split(' ')
        r = int(rm)

        if d == 'R':
            dxy = (1, 0)
        elif d == 'L':
            dxy = (-1, 0)
        elif d == 'U':
            dxy = (0, 1)
        else:
            dxy = (0, -1)

        for _ in range(r):

            # diff = dxy
            # for i in range(1, len(rope)):
                
            #     rope[i - 1], nt = move(rope[i - 1], rope[i], diff)
            #     diff = (nt[0] - rope[i][0], nt[1] - rope[i][1])

            # rope[-1] = nt
            # ts.add(rope[-1])
            h = rope[0]
            rope[0] = (h[0] + dxy[0], h[1] + dxy[1])
            for i in range(1, len(rope)):

                h, t = rope[i - 1], rope[i]
                rope[i] = move2((h[0], h[1]), t)

            ts.add(rope[-1])

        # print(rope)

    return ts

def move(h, t, dxy):

    dx, dy = dxy
    nh = (h[0] + dx, h[1] + dy)

    if dx != 0 and dy != 0:
        ox, oy = nh[0] - t[0], nh[1] - t[1]

        if abs(ox) > abs(oy):
            t = (t[0] + norm(ox), h[1])
        elif abs(ox) < abs(oy):
            t = (h[0], t[1] + norm(oy))
        else:
            t = h

    elif dx != 0:
        ox = nh[0] - t[0]
        if abs(ox) == 2:
            t = h
    elif dy != 0:
        oy = nh[1] - t[1]
        if abs(oy) == 2:
            t = h

    return nh, t

def move2(h, t):

    dx, dy = (t[0] - h[0], t[1] - h[1])
    nt = t
    if abs(dx) == 2 and abs(dy) == 2:
        nt = (h[0] + norm(dx), h[1] + norm(dy))
        
    if abs(dx) == 2 and abs(dy) == 1:
        nt = (h[0] + norm(dx), h[1])
    if abs(dx) == 2 and abs(dy) == 0:
        nt = (h[0] + norm(dx), h[1])

    if abs(dx) == 1 and abs(dy) == 2:
        nt = (h[0], h[1] + norm(dy))
    if abs(dx) == 0 and abs(dy) == 2:
        nt = (h[0], h[1] + norm(dy))

    return nt

def norm(x):

    return max(-1, min(1, x))


if __name__ == '__main__':

    TEST = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
    TEST2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''
    
    assert norm(2) == 1
    assert norm(0) == 0
    assert norm(-1) == -1
    assert norm(-2) == -1

    with open('09.txt') as f:
        inp = f.read()


    res = p2(TEST)
    print(res, len(res))

    assert len(res) == 1

    res = p2(inp)
    print(res, len(res))