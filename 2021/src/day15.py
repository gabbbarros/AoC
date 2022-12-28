import re
import queue

dir = [(1,0),(0,1),(-1,0),(0,-1)]

def main():
    sensors = []
    with open("sminput","r") as f:
        for x in f:
            x = x.strip().replace(","," ")
            x = re.split("[= :]" ,x)
            l = []
            for a in x:
                try:
                    l.append(int(a))
                except ValueError:
                    pass
            sensors.append(l)

    largeDic = {}
    dic = {}
    row = 2000000
    frontier = queue.Queue()

    distDic = {}
    minX = 100000
    maxX = 0
    for s in sensors:
        dist = manh(s[0], s[1], s[2], s[3])
        distDic[(s[0], s[1])] = dist
        if s[0] - dist < minX:
            minX = s[0] - dist
        if s[0] + dist > maxX:
            maxX = s[0] + dist

    m = 0
    n = 4000000
    print(part1(minX, maxX, sensors, row))
    print(part2(0,n,sensors,distDic))



def part2(min,max,sensors,distDic):
    result = 0

    for s in range(len(sensors)):
        print(f"{sensors[s]} {distDic[(sensors[s][0],sensors[s][1])]}")
        i = sensors[s][0]
        j = sensors[s][1] - distDic[(sensors[s][0],sensors[s][1])] - 1
        found = False
        while j <= sensors[s][1]:
            found = False
            if j >= min and j <= max and i >= min and i <=max:
                for r in range(len(sensors)):
                    if manh(i,j,sensors[r][0],sensors[r][1]) <= distDic[(sensors[r][0],sensors[r][1])]:
                        found = True
                        r = len(sensors)
                        break
                if not found:
                    return (i * 4000000) + j
            j += 1
            i += 1

        i = sensors[s][0]
        j = sensors[s][1] + distDic[(sensors[s][0],sensors[s][1])] + 1
        while j >= sensors[s][1]:
            found = False
            if j >= min and j <= max and i >= min and i <=max:
                for r in range(len(sensors)):
                    if manh(i, j, sensors[r][0], sensors[r][1]) <= distDic[(sensors[r][0], sensors[r][1])]:
                        found = True
                        r = len(sensors)
                        break
                if not found:
                    return (i * 4000000) + j
            j -= 1
            i += 1

        i = sensors[s][0] - distDic[(sensors[s][0],sensors[s][1])] - 1
        j = sensors[s][1]
        while i <= sensors[s][0]:
            found = False
            #print(f"\t3: {i} {j} {sensors[s]}")
            if j >= min and j <= max and i >= min and i <=max:
                for r in range(len(sensors)):
                    if manh(i, j, sensors[r][0], sensors[r][1]) <= distDic[(sensors[r][0], sensors[r][1])]:
                        found = True
                        r = len(sensors)
                        break
                if not found:
                    return (i * 4000000) + j
            j += 1
            i += 1

        i = sensors[s][0] + distDic[(sensors[s][0],sensors[s][1])] + 1
        j = sensors[s][1]
        while i >= sensors[s][0]:
            found = False
            if j >= min and j <= max and i >= min and i <=max:
                for r in range(len(sensors)):
                    if manh(i, j, sensors[r][0], sensors[r][1]) <= distDic[(sensors[r][0], sensors[r][1])]:
                        found = True
                        r = len(sensors)
                        break
                if not found:
                    return (i * 4000000) + j
            j += 1
            i -= 1

    return -1


def part1(minX, maxX, sensors, row):
    minX = 100000
    maxX = 0
    maxDic = {}
    beacons = {}
    for s in sensors:
        dist = manh(s[0], s[1], s[2], s[3])
        if s[3] == row:
            beacons[(s[2], s[3])] = 1
        maxDic[(s[0], s[1])] = dist
        if s[0] - dist < minX:
            minX = s[0] - dist
        if s[0] + dist > maxX:
            maxX = s[0] + dist

    count = 0
    for i in range(minX, maxX + 1):
        print(i)
        try:
            n = (i, row)
            a = beacons[n]
            continue
        except:
            for s in maxDic:
                d = manh(s[0], s[1], i, row)
                if d <= maxDic[s]:
                    count += 1
                    break

def manh(x1,y1,x2,y2):
    return (max(x1,x2)-min(x1,x2)) + (max(y1,y2)-min(y1,y2))

if __name__ == "__main__":
    main()