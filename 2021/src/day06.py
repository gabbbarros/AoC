f = open("sminput","r")

def findpackage(x, length):
    i = length-1
    l = []
    while i < len(x):
        l.clear()
        for j in range(length):
            if x[i - j] not in l:
                l.append(x[i - j])

        if len(l) == length:
            return i + 1
        i += 1

for x in f:
    #Part 1
    print(findpackage(x,4))
    #Part 2
    print(findpackage(x, 14))