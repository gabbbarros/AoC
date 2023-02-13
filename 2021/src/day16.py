#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
from queue import PriorityQueue
from queue import SimpleQueue
from math import pow

class Valve:
    def __init__(self, name, flow, to):
        self.name=  name
        self.flow = flow
        self.to = to
        self.open = False

    def __repr__(self):
        return f"{self.name}: {self.flow} ({self.open}) -> {self.to}"

class State:
    def __init__(self, t, opened, current, value):
        self.opened = opened
        self.t = t
        self.current = current
        self.value = value

    def __repr__(self):
        return f"{self.t}  > {self.current} {self.opened:b} v: {self.value}"

def printValves(valves,valvesDic,dist):
    for i in range(len(valves)):
        print(f"\t{valvesDic[i].name}",end="")
    print("")
    for i in range(len(valves)):
        print(f"{valvesDic[i].name}\t", end="")
        for j in range(len(valves)):
            print(f"{dist[i][j]}\t", end="")
        print("")

def main():
    valvesDic = {}
    valves = []

    with open("../input/day16.txt","r") as f:
        valves.append("")
        for x in f:
            x = x.strip().replace(",","").replace(";","").replace("="," ").split(" ")
            l = []
            for i in range(10, len(x)):
                l.append(x[i])
            #forcing AA to be the first value because don't want to swift all bitwise ops
            if x[1] == "AA":
                valves[0] = Valve(x[1],int(x[5]),l)
                valvesDic[0] = valves[0]
                valvesDic[valves[0].name] = 0
            else:
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

    for k in range(len(valves)):
        for i in range(len(valves)):
            for j in range(len(valves)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    #printValves(valves,valvesDic,dist)
    start = 0
    for v in range(len(valves)):
        if valves[v].name == "AA":
            start = v
            break

    useful = []
    for v in range(len(valves)):
        if valves[v].flow > 0 and v != start:
            useful.append(v)

    #part 1
    print(f"Part 1: {calculate_paths(valves,dist,start,useful,30)[0]}")

    #part 2
    r, all = calculate_paths(valves,dist,start,useful,26)

    pairs=[]
    max = 0

    for a in all:
        if a != 0:
            for b in all:
                if b != 0:
                    if a&b == 0:
                        pairs.append((a,b))

    for pair in pairs:
        if max < all[pair[0]]+all[pair[1]]:
            max = all[pair[0]]+all[pair[1]]
    print(f"Part 2: {max}")



def calculate_paths(valves,dist,cur,possible,t):
    amounts = len(possible)
    size = int(pow(2,amounts))
    states = SimpleQueue()
    states.put(State(t,0,cur,0))
    visited = {}
    while not states.empty():
        cur_state = states.get()
        next = [a for a in possible if cur_state.opened & (1 << a) == 0]
        if cur_state.t <= 0 or len(next) == 0:
            try:
                if visited[cur_state.opened] < cur_state.value:
                    visited[cur_state.opened] = cur_state.value
            except:
                visited[cur_state.opened] = cur_state.value

        else:
            for n in next:
                if dist[cur_state.current][n] < cur_state.t - 1:
                    states.put(State(cur_state.t - dist[cur_state.current][n] - 1,
                                     cur_state.opened | (1<<n),
                                     n,
                                     cur_state.value + ((cur_state.t - dist[cur_state.current][n] - 1)*valves[n].flow)))

            try:
                if visited[cur_state.opened] < cur_state.value:
                    visited[cur_state.opened] = cur_state.value
            except:
                visited[cur_state.opened] = cur_state.value


    rest = 0
    index = 0
    for a in visited:
        if visited[a] > rest:
            rest = visited[a]
            index = a
    return visited[index], visited


if __name__ == "__main__":
    main()