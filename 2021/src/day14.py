
def find_height(f):
    h = 0
    minw = 100000000000000000000
    maxw = 0
    l = []
    for x in f:
        l.append(x)
        x = x.strip().split(" -> ")
        for i in range(len(x)):
            a = [int(y) for y in x[i].split(",")]
            if a[1] > h:
                h = a[1]
            if a[0] > maxw:
                maxw = a[0]
            if a[0] < minw:
                minw = a[0]
    return h+2,minw-1,maxw+1,l

def main():
    cave = []
    m = 0
    n = 5000000
    with open("sminput") as f:
        h,min,max,f = find_height(f)
    w = max - min

    neededWidth = 0
    for i in range(h+1):
        neededWidth =1 + (2*i)
    w = neededWidth+2

    min -= int(neededWidth/2)
    w = int(w*1.75)

    for a in range(h):
        l = []
        cave.append(l)
        for b in range(w):
            l.append(0)

    for x in f:
        x = x.strip().split(" -> ")
        for i in range(len(x) - 1):
            a = [int(y) for y in x[i].split(",")]
            b = [int(y) for y in x[i+1].split(",")]
            if a[0] > m:
                m = a[0]
            if b[0] > m:
                m = b[0]
            if a[0] < n:
                n = a[0]
            if b[0] < n:
                n = b[0]
            a[0] -= min
            b[0] -= min

            if a[0] == b[0]:
                if b[1] < a[1]:
                    z = b[1]
                    b[1] = a[1]
                    a[1] = z
                while a[1] <= b[1]:
                    cave[a[1]][a[0]] = 1
                    a[1] += 1
            else:
                if b[0] < a[0]:
                    z = b[0]
                    b[0] = a[0]
                    a[0] = z
                while a[0] <= b[0]:
                    cave[a[1]][a[0]] = 1
                    a[0] += 1

    start = [0,500-min]

    secondCave = []
    for a in range(len(cave)):
        l = []
        for b in range(len(cave[a])):
            l.append(cave[a][b])
        secondCave.append(l)

    print(f"Part 1 {search1(start[1],start[0],cave,h,w)[0]}")
    print(f"Part 2 {search(start[1],start[0],secondCave,h,w)}")



def search1(x,y,cave,h,w,dep=1):
    cave[y][x] = 2
    if y+1 >= h:
        return 1-dep,True
    sum = 1
    found = False
    if cave[y+1][x] == 0:
        a,found = search1(x,y+1,cave,h,w,dep+1)
        sum+=a
        if found:
            return sum,found
    if x > 0 and cave[y+1][x-1] == 0:
        a,found = search1(x - 1, y + 1, cave, h, w,dep+1)
        sum+=a
        if found:
            return sum,found
    if x < w-1 and cave[y+1][x+1] == 0:
        a,found = search1(x + 1, y + 1, cave, h, w,dep+1)
        sum+=a
        if found:
            return sum,found
    return sum,False

def search(x,y,cave,h,w):
    cave[y][x] = 2
    if y+1 >= h:
        return 1
    sum = 1
    if cave[y+1][x] == 0:
        sum += search(x,y+1,cave,h,w)
    if x > 0 and cave[y+1][x-1] == 0:
        sum += search(x - 1, y + 1, cave, h, w)
    if x < w-1 and cave[y+1][x+1] == 0:
        sum += search(x + 1, y + 1, cave, h, w)
    return sum

if __name__ == "__main__":
    main()