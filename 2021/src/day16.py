#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
from queue import PriorityQueue

class Valve:
    def __init__(self, name, flow, to):
        self.name=  name
        self.flow = flow
        self.to = to
        self.open = False

    def __repr__(self):
        return f"{self.name}: {self.flow} ({self.open}) -> {self.to}"



def main():
    valvesDic = {}
    valves = []

    with open("../input/day16.txt","r") as f:
        for x in f:
            x = x.strip().replace(",","").replace(";","").replace("="," ").split(" ")
            l = []
            for i in range(10,len(x)):
                l.append(x[i])
            valves.append(Valve(x[1],int(x[5]),l))
            valvesDic[len(valves)-1]=valves[len(valves)-1]
            valvesDic[valves[len(valves)-1].name]=len(valves)-1

    useful = PriorityQueue()
    for v in range(len(valves)):
        if valves[v].flow > 0:
            useful.put((valves[v].flow,v))

    dist = []
    for i in range(len(valves)):
        l = []
        for j in range(len(valves)):
            l.append(100000000)
        dist.append(l)

    for i in range(len(valves)):
        dist[i][i] = 0
    for i in range(len(valves)):
        for v in valves[i].to:
            dist[i][valvesDic[v]] = 1

    for i in range(len(valves)):
        for j in range(i+1,len(valves)):
            for k in range(i+1,j):
                print(f"{i} {j} {k} : {dist[i][j]} {dist[i][k] + dist[k][j]}")
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    for i in range(len(valves)):
        print(f"\t{valvesDic[i].name}",end="")
    print("")
    for i in range(len(valves)):
        print(f"{valvesDic[i].name}\t", end="")
        for j in range(len(valves)):
            print(f"{dist[i][j]}\t", end="")
        print("")



    t = 30
    cur = 0
    next = None
    s = 0
    total = 0
    while t > 0:
        #while not useful.empty():
        #    useful.get()
        print(f">{t} in {cur} {valves[cur].name}")
        aux = 0
        for v in range(len(valves)):
            if not valves[v].open and valves[v].flow > 0:
                print(f"\tChc {valves[v].name} ({valves[v].flow}) {valves[v].flow*(t-dist[cur][v])}")
                if next is None or valves[v].flow*(t-dist[cur][v]) > aux:
                    next = v
                    aux = valves[v].flow*(t-dist[cur][v])
                    print(f"\t\tnext {next} {valves[next].name} dist {dist[cur][v]}")
                #useful.put((valves[v].flow*(t-dist[cur][v]), v))
        total += s*dist[cur][v]
        t = t - dist[cur][v]
        s+=valves[next].flow
        valves[next].open = True
        cur = next


        print(f"\t t {t} next {next} total {total} s {s}")
        t-=1
    print(total)
    exit(0)
    time = 30
    cur = "AA"
    opened = set()
    curFlow = 0
    curSum = 0
    stack = []
    while time > 0:
        n = valves[cur]

        if n.open  == False:
            n.open = True
            opened.add(opened)
            n.open = True
            curFlow+=n.flow
        else:
            next = None
            for c in n.to:
                child = valves[c]
                if child not in opened and child.flow > 0:
                    if next == None:
                        next = child
                    elif next.flow < child.flow:
                        next = child
            if next != None:
                cur = next
                stack.append(cur)
            else:
                cur = stack.pop()

        curSum += curFlow

        time -= 1
    print(curSum)

def calc(a, b, valves, dist):
    pass

if __name__ == "__main__":
    main()