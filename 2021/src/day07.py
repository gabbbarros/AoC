f = open("sminput","r")

class Node() :
    name = None
    parent = None
    children = None
    files = None
    size = -1
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def calculateSize(self):
        self.size = 0
        for x in self.children:
            self.size += self.children[x].calculateSize()
        for x in self.files:
            self.size += self.files[x]
        return self.size

def sumSize(node, max):
    sum = 0
    if node.size <= max:
        sum+=node.size
    for x in node.children:
        sum += sumSize(node.children[x], max)
    return sum

def sumSizeAtLeast(node,min):
    res = -1
    if node.size >= min:
        res = node.size
    elif node.size < min:
        return -1
    for x in node.children:
        child = sumSizeAtLeast(node.children[x], min)
        if child != -1 and child < res:
            res = child
    return res

def main():
    root = Node("/",None)
    current = root
    input = []
    for x in f:
        x = x.replace("\n","").split(" ")
        input.append(x)

    i = 0
    while i < len(input):
        x = input[i]
        if x[0] == "$":
            # command
            if x[1] == "ls":
                j = i+1
                while j < len(input):
                    if input[j][0] != "$":
                        if input[j][0] == "dir":
                            node = Node(input[j][1], current)
                            current.children[node.name] = node
                        else:
                            current.files[input[j][1]] = int(input[j][0])
                    else:
                        i = j-1
                        break
                    j+=1
                if j == len(input):
                    break
            elif x[1] == "cd":
                if x[2] == "/":
                    current = root
                elif x[2] == "..":
                    current =  current.parent
                else:
                    current = current.children[x[2]]
        else:
            #should never happen
            print(f"UNEXPECTED {x}")
            pass
        i+=1

    root.calculateSize()

    needed = 30000000 - (70000000 - root.size)
    print(f"Part 1: {sumSize(root,100000)}")
    print(f"Part 2"
          f": {sumSizeAtLeast(root, needed)}")


if __name__ == "__main__" :
    main()