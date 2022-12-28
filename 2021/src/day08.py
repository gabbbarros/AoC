
def countIfVis(x,y,trees):
    if(trees[y-1][x] < trees[y][x] or trees[y+1][x] < trees[y][x] or
            trees[y][x-1] < trees[y][x] or trees[y][x+1] < trees[y][x]):
        print(f"{x} {y} {trees[y][x]}")
        return 1
    else:
        return 0

def calcVis(x,y,trees,mat,w,h):
    vis = [True,True,True,True]
    for y2 in range(0,y-1).__reversed__():
        if mat[y2][x] != 0:
            vis[0] = False
            break
    for x2 in range(0,x-1).__reversed__():
        if mat[y][x2] != 0:
            vis[3] = False
            break
    for x2 in range(x+1,w):
        if trees[y][x2] >= trees[y][x]:
            vis[1] = False
            break
    for y2 in range(y+1,h):
        if trees[y2][x] >= trees[y][x]:
            vis[2] = False
            break
    if vis[0] or vis[1] or vis[2] or vis[3]:
        return 0
    else:
        return 1

def calcMatrix1(trees, w,h):
    mat = []
    for y in range(h):
        mat.append([])
        for x in range(w):
            mat[y].append(-1)
    for x in range(w):
        mat[0][x] = 0
        mat[h-1][x] = 0
    for y in range(h):
        mat[y][0] = 0
        mat[y][w-1] = 0


    for y in range(1, h - 1):
        max = trees[y][0]
        for x in range(1, w):
            if max < trees[y][x] and trees[y][x-1] < trees[y][x]:
                mat[y][x] = 0
            if trees[y][x] > max:
                max = trees[y][x]

    for y in range(1,h-1):
        max = trees[y][w-1]
        for x in range(0,w-1).__reversed__():
            if trees[y][x+1] < trees[y][x] and max < trees[y][x]:
                mat[y][x] = 0
            if trees[y][x] > max:
                max = trees[y][x]

    for x in range(1, w-1):
        max = trees[0][x]
        for y in range(1, h):
            if trees[y - 1][x] < trees[y][x] and max < trees[y][x]:
                mat[y][x] = 0
            if trees[y][x] > max:
                max = trees[y][x]

    for x in range(1, w - 1):
        max = trees[h-1][x]
        for y in range(0,h-1).__reversed__():
            if trees[y+1][x] < trees[y][x] and max < trees[y][x]:
                mat[y][x] = 0
            if trees[y][x] > max:
                max = trees[y][x]

    count = 0
    for y in range(h):
        for x in range(w):
            if(mat[y][x] == 0):
                count+=1
    return count

def calcSpec(r1,r2,trees, x,y,varyY, reverse=False):
    c = 0
    ran = range(r1, r2)
    if reverse:
        ran = ran.__reversed__()
    for z in ran:
        c += 1
        if varyY:
            if trees[z][x] >= trees[y][x]:
                break
        else:
            if trees[y][z] >= trees[y][x]:
                break
    return c

def calc(x,y,trees,w,h) :
    """for z in range(0, y - 1).__reversed__():
           c+=1
           if trees[z][x] >= trees[y][x]:
               break
       """
    s = 1
    # up
    c = calcSpec(0, y, trees, x, y, True, True)
    if c == 0:
        return 0
    s = s * c

    # down
    c = calcSpec(y + 1, h, trees, x, y, True)
    if c == 0:
        return 0
    s = s * c

    # left
    c = calcSpec(0, x, trees, x, y, False, True)
    if c == 0:
        return 0
    s = s * c

    # down
    c = calcSpec(x + 1, w, trees, x, y, False)
    if c == 0:
        return 0
    s = s * c
    return s




def calcMatrix2(trees, w,h):
    mat = []
    for y in range(h):
        mat.append([])
        for x in range(w):
            mat[y].append(-1)


    for x in range(w):
        mat[0][x] = 0
        mat[h-1][x] = 0
    for y in range(h):
        mat[y][0] = 0
        mat[y][w-1] = 0

    for y in range(h):
        for x in range(w):
            if mat[y][x] == -1:
                mat[y][x] = calc(x,y,trees,w,h)

    for y in range(h):
        for x in range(w):
            print(f"{mat[y][x]}:({trees[y][x]})",end=" ")
        print("")

    max = 0
    for y in range(h):
        for x in range(w):
            if mat[y][x]  > max:
                max = mat[y][x]
    return max




def main():
    f = open("sminput","r")
    trees = []
    for x in f:
        x = x.replace("\n","")
        l = []
        for i in x:
            l.append(int(i))
        trees.append(l)

    w = len(trees[0])
    h = len(trees)

    #print(f"Part 1 : {calcMatrix1(trees, w, h)}")
    print(f"Part 2 : {calcMatrix2(trees, w, h)}")


if __name__=="__main__":
    main()