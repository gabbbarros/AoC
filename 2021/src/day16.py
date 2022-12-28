#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

class Valve:
    def __init__(self, name, flow, to):
        self.name=  name
        self.flow = flow
        self.to = to

    def __repr__(self):
        return f"{self.name}: {self.flow} -> {self.to}"



def main():
    valves = {}
    with open("sminput","r") as f:
        for x in f:
            x = x.strip().replace(",","").replace(";","").replace("="," ").split(" ")
            l = []
            for i in range(10,len(x)):
                l.append(x[i])
            valves[x[1]] = Valve(x[1],int(x[5]),l)

    time = 30
    cur = "AA"
    opened = set()
    while time > 0:
        n = valves[cur]
        opened.add(opened)
        next = None
        for child in n.to:
            if child not in opened and child.flow > 0:
                if next == None:
                    next = child
                elif next.flow < child.flow:
                    next = child



        time -= 1




if __name__ == "__main__":
    main()