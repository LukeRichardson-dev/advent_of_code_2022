from dataclasses import dataclass


TEST = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

@dataclass
class File:

    size: int
    name: str

@dataclass
class Directory:

    name: str
    subdirs: list
    files: list[File]

    def size(self, acc=0):

        for i in self.subdirs:
            acc = i.size(acc)

        for i in self.files:
            acc += i.size

        return acc

    def add_at(self, path, obj, is_file):
        if not path:
            if is_file:
                self.files.append(obj)
            else:
                self.subdirs.append(obj)

            return
        
        for directory in self.subdirs:
            if directory.name == path[0]:
                directory.add_at(path[1:], obj, is_file)
                break

    def small_size(self, maximum, acc=0):
        size = self.size()
        if size < maximum:
            acc += size

        for i in self.subdirs:
            acc = i.small_size(maximum, acc)
        
        return acc

    def free(self, target, cmin=70_000_000):
        size = self.size()
        if target < size < cmin:
            cmin = size

        for i in self.subdirs:
            cmin = i.free(target, cmin)

        return cmin



def p1(inp):
    location = []
    root = Directory('/', [], [])

    for line in inp.split('\n'):

        if line[0] == '$':

            _, command, *arg = line.split(' ')
            if command == 'cd':
                if arg[0] == '/': continue
                if arg[0] == '..':
                    location.pop()
                    continue
                
                location.append(arg[0])

        else:

            pre, post = line.split(' ')

            if pre == 'dir':
                root.add_at(location, Directory(post, [], []), False)
                continue

            size = int(pre)
            root.add_at(location, File(size, post), True)

    return root

if __name__ == '__main__':
    with open('07.txt') as f:
        inp = f.read()

    rt = p1(TEST)

    free = 7 * 10 ** 7 - rt.size()
    print(3 * 10 ** 7 -  free)
    print(rt.free(30_000_000 - free))