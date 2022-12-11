TEST = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

def should_display(cycle):

    return cycle % 40 == 20

def parse(inp: str):

    for i in inp.split('\n'):
        op, *args = i.split(' ')
        yield 0

        if op == 'addx':
            inc = int(args[0])
            yield inc

def process_instr(instr, condition):
    x = 1
    count = 1
    for i in instr:
        count += 1
        x += i
        if condition(count):
            yield x * count

def accumulate(iterable, start=1):
    a = start
    for i in iterable:
        yield a
        a += i

def render_instr(instr):

    for idx, x in enumerate(accumulate(instr)):

        pos = idx % 40 
        # print(pos, x, x - pos)
        yield '#' if -1 <= x - pos <= 1 else '.'

def display(iterable, width=40):

    for idx, o in enumerate(iterable):
        print(o, end='')
        if idx % width + 1 == width:
            print()

if __name__ == '__main__':

    assert not should_display(19)
    assert not should_display(21)
    assert should_display(20) 
    assert not should_display(40)
    assert should_display(60)

    instr = parse(TEST)
    assert sum([*instr][:20]) + 1 == 21

    instr = parse(TEST)
    assert sum(process_instr(instr, should_display)) == 13140

    with open('10.txt') as f:
        inp = f.read()

    instr = parse(inp)
    res = sum(process_instr(instr, should_display))
    print(res)

    instr = parse(TEST)
    rendered = render_instr(instr)
    display(rendered)

    print()
    instr = parse(inp)
    rendered = render_instr(instr)
    display(rendered)
    