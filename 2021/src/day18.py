from copy import deepcopy

import numpy as np

def main():
    input = []
    with open("../input/day18.txt") as f:
        for x in f:
            x = x.strip().split(",")
            input.append((int(x[0]),int(x[1]),int(x[2])))

    print(f"Part 1 {part1(input)}")
    print(f"Part 2 {part2(input)}")


def part2(input):
    maxV = [0,0,0]
    for x in input:
        for i in range(3):
            if maxV[i] < x[i]:
                maxV[i] = x[i]
    xs = maxV[0]+1
    ys = maxV[1]+1
    zs = maxV[2]+1
    color = np.zeros(([xs, ys, zs]), dtype=np.int8)

    for x in input:
        color[x[0], x[1], x[2]] = 1
    color = fill(color, xs, ys, zs, (0,0,0), 2)

    total = part1(input)
    last = 3
    for i in range(xs):
        for j in range(ys):
            for z in range(zs):
                if color[i,j,z] == 0:
                    color = fill(color, xs, ys, zs, (i,j,z), last)
                    last+=1

    dic = {}
    for i in range(xs):
        for j in range(ys):
            for z in range(zs):
                if color[i,j,z] >= 3:
                    if color[i,j,z] in dic:
                        dic[color[i, j, z]].append((i, j, z))
                    else:
                        dic[color[i, j, z]] = [(i,j,z)]
    for d in dic:
        v = part1(dic[d])
        total -= v
    return total

def fill(color, xs, ys, zs, start, filler):
    front = [start]

    while len(front) > 0:
        cur = front.pop()
        if color[cur[0], cur[1], cur[2]] == 0:
            color[cur[0], cur[1], cur[2]] = filler
            if cur[0] > 0:
                if color[cur[0] - 1, cur[1], cur[2]] == 0:
                    front.append((cur[0] - 1, cur[1], cur[2]))
            if cur[0] + 1 < xs:
                if color[cur[0] + 1, cur[1], cur[2]] == 0:
                    front.append((cur[0] + 1, cur[1], cur[2]))

            if cur[1] > 0:
                if color[cur[0], cur[1] - 1, cur[2]] == 0:
                    front.append((cur[0], cur[1] - 1, cur[2]))
            if cur[1] + 1 < ys:
                if color[cur[0], cur[1] + 1, cur[2]] == 0:
                    front.append((cur[0], cur[1] + 1, cur[2]))

            if cur[2] > 0:
                if color[cur[0], cur[1], cur[2] - 1] == 0:
                    front.append((cur[0], cur[1], cur[2] - 1))
            if cur[2] + 1 < zs:
                if color[cur[0], cur[1], cur[2] + 1] == 0:
                    front.append((cur[0], cur[1], cur[2] + 1))

    return color

def part1(input):
    count = {}
    for x in input:
        cur = 6
        for a in count:
            same = 0
            dif_by_1 = 0
            for i in range(3):
                if a[i] == x[i]:
                    same+=1
                elif abs(a[i]-x[i])==1:
                    dif_by_1+=1
            if same ==2 and dif_by_1==1:
                cur-=1
                count[a] = count[a]-1
        count[x] = cur

    total = 0
    for a in count:
        total+=count[a]

    return total

if __name__ == "__main__":
    main()