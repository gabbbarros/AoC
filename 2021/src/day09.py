
def updateTail(head,tail):
    dist = (head[0] - tail[0], head[1] - tail[1])
    sum = abs(dist[0])+abs(dist[1])

    if(sum >2):
        if dist[0] > 0:
            x = 1
        elif dist[0] < 0:
            x = -1
        else:
            x = 0

        tail[0] += 1 * x
        if dist[1] > 0:
            x = 1
        elif dist[1] < 0:
            x = -1
        else:
            x = 0
        tail[1] += 1 * x
    elif(abs(dist[0]) ==2 or abs(dist[1]) == 2):
        if dist[0] > 0:
            x = 1
        elif dist[0] < 0:
            x = -1
        else:
            x = 0

        tail[0] += 1 * x
        if dist[1] > 0:
            x = 1
        elif dist[1] < 0:
            x = -1
        else:
            x = 0
        tail[1] += 1 * x

def printMap(nodes):
    global map, w, h
    for a in range(h):
        for b in range(w):
            printed = False
            for x in range(len(nodes)):
                if a == nodes[x][1] and b == nodes[x][0]:
                    print(f"{x}",end="")
                    printed = True
                    break
            if not printed:
                print(".",end="")
        print("")

def move(x,y,nodes,repeat,dic):
    for a in range(repeat):
        nodes[0][0] += x
        nodes[0][1] += y
        for j in range(len(nodes)-1):
            updateTail(nodes[j], nodes[j+1])
        for j in dic:
            dic[j].add((nodes[j][0], nodes[j][1]))
    #printMap(nodes)

def main():
    global map, w, h
    map = []
    w = 20
    h = 20
    for a in range(h):
        map.append([])
        for b in range(w):
            map[a].append(0)
    start = [10,10]
    knots = 10
    nodes = []
    for a in range(knots):
        nodes.append(start.copy())

    dic = {1:set(),knots-1: set()}
    for a in dic:
        dic[a].add((start[0],start[1]))

    with open("sminput","r") as f:
        for x in f:
            x = x.strip().split(" ")
            print(f"{x} : {int(x[1])}")
            if x[0] == "R":
                move(1,0,nodes,int(x[1]),dic)
            elif x[0] == "U":
                move(0,-1,nodes,int(x[1]),dic)
            elif x[0] == "D":
                move(0,1,nodes,int(x[1]),dic)
            elif x[0] == "L":
                move(-1,0,nodes,int(x[1]),dic)

    print(f"Part 1: {len(dic[1])}")
    print(f"Part 2: {len(dic[knots-1])}")
    print(dic)


if __name__ == "__main__":
    main()