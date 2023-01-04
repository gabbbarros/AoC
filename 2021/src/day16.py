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

    for k in range(len(valves)):
        for i in range(len(valves)):
            for j in range(len(valves)):
                #print(f"{i} {j} {k} : {dist[i][j]} {dist[i][k] + dist[k][j]}")
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    printValves(valves,valvesDic,dist)
    start = 0
    for v in range(len(valves)):
        if valves[v].name == "AA":
            start = v
            break

    useful = []
    for v in range(len(valves)):
        if valves[v].flow > 0 and v != start:
            useful.append(v)
    #print(part1(valves,valvesDic,dist,start,useful,30,[],0,0,[start]))
    print(part2(valves,valvesDic,dist,start,start,useful,26,26,26,0,0,[start],0,0))

def p(d):
    for i in range(d):
        print("\t",end="")

def part2(valves,valvesDic,dist,curP, curE,possible,t,travel1,travele,flowp,flowe, vis,d,s):

    p(d)
    print(f"> t {t} : in {curP} ({travel1}) and {curE} ({travele}) ( => {vis}) [sum {s}] pos: {possible}")
    if t <= 0:
        return 0
    """if len(possible) == 0:
        ret = 0
        if travel1 > 0 and t - travel1 > 0:
            ret += (t - travel1) * flowp
        if travele > 0 and t - travele > 0:
            ret += (t - travele) * flowe
        ret += (t*s)

        p(d)
        print(f"ret {ret}")
        return ret"""
    returnMax = 0
    if travel1 == t and travele == t:
        if len(possible) == 0:
            #returnMax = (t) * (flowp + flowe)#(t+1) * (flowp + flowe)
            #p(d)
            #print(f"\tAA {max} ")
            pass
        else:
            # do both
            for indi in range(len(possible)):
                for indj in range(len(possible)):
                    if indi == indj:
                        continue
                    i = possible[indi]
                    j = possible[indj]

                    vv = []
                    for a in vis:
                        vv.append(a)
                    if curP not in vv:
                        vv.append(curP)
                    if curE not in vv:
                        vv.append(curE)
                    aux = []
                    for k in possible:
                        if k != i and k != j:
                            aux.append(k)
                    #vv.append(i)
                    #vv.append(j)

                    newt1 = t - dist[curP][i] - 1# - 1
                    newt2 = t - dist[curE][j] - 1# - 1

                    v = 0
                    if newt1 > 0:
                        v += newt1 * valves[i].flow
                    if newt2 > 0:
                        v += newt2 * valves[j].flow
                        #t * (flowp + flowe)#(t+1) * (flowp + flowe)
                    if newt1 > 0 or newt2 > 0:

                        """if newt1 > 0:
                            v += valves[i].flow * (newt1)
                        if newt2 > 0:
                            v += valves[j].flow * (newt2)"""
                        if newt1 > newt2:

                            #v += ((dist[curP][i] + 1) * (s+flowp+flowe))
                            #p(d)
                            #print(f"\tA {v}  ({travel1}) ({travele})  {t} {curP} {curE} to {i} {j} {aux} newt1 {newt1} newt {newt2} {s} {v} dis {dist[curP][i]} dis {dist[curE][j]} ?? {dist[curE][j] - dist[curP][i]}")
                            v += part2(valves, valvesDic, dist, i, j, aux, newt1, newt1, newt2, valves[i].flow,valves[j].flow,vv,d + 1, s + flowe+flowp)
                        elif newt2 > newt1:
                            #v += ((dist[curE][j] + 1) * (s+flowp+flowe))
                            #p(d)
                            #print(f"\tB  {v}  ({travel1})  ({travele}) {t} {curP} {curE} to {i} {j} {aux} newt1 {newt1} newt {newt2} {s} {v} dis {dist[curP][i]} dis {dist[curE][j]}")
                            v += part2(valves, valvesDic, dist, i, j, aux, newt2, newt1, newt2,valves[i].flow,valves[j].flow,vv, d + 1, s+ flowe+flowp)
                        else:
                            #v += ((dist[curE][j] + 1) * (s+flowp+flowe))
                            #p(d)
                            #print(f"\tC {v} ({travel1}) ({travele}) {t} {curP} {curE} to {i} {j} {aux }newt1 {newt1} newt {newt2} {s} {v}dis {dist[curP][i]} dis {dist[curE][j]}")
                            v += part2(valves, valvesDic, dist, i, j, aux, newt2, newt1, newt2, valves[i].flow,valves[j].flow,vv, d + 1, s + flowe+flowp)

                    else:
                        pass
                        #v = t * s
                        #p(d)
                        #print(f"\t {cur} to {i} {aux} no t {v}")
                    """if newt1 > 0 and newt2 > 0:
                        v = ((dist[curP][i] + 1) * s) + ((dist[curE][j] + 1) * s)
                        # p(d)
                        # print(f"\t {cur} to {i} {aux} newt{newt} {s} {v}")
                        v += part2(valves, valvesDic, dist, i, aux, newt1, l, d + 1, s + valves[i].flow, vv)
                    else:
                        v = t * s"""
                        #
                    if returnMax < v:
                        #p(d)
                        #print(f"! max > {returnMax} {v}")
                        returnMax = v
                    vv.pop()
    elif travel1 == t:
        if len(possible) == 0:
            pass
            """max = ((t) * flowp)#((t+1) * flowp)
            if travele > 0:
                p(d)
                print(f"\tDD {max} to {curP} {curE} {t-travele} newt{t-travele} ")
                max += + part2(valves, valvesDic, dist, curP, curE, [], t-travele, travel1-travele, 0, 0,
                                   flowe, vis, d + 1, s + flowp)
            else:
                p(d)
                print(f"\tDD {max}")"""
        else:
            for indi in range(len(possible)):
                i = possible[indi]

                vv = []
                for a in vis:
                    vv.append(a)

                vv.append(curP)
                aux = []
                for k in possible:
                    if k != i:
                        aux.append(k)
                #vv.append(i)

                newt1 = t - dist[curP][i] - 1# - 1
                newt2 = travele

                v = 0#(t) * (flowp)#(t+1) * (flowp)
                if newt1 > 0 :
                    v += newt1 * valves[i].flow
                    #p(d)
                    # print(f"\t {cur} to {i} {aux} newt{newt} {s} {v}")
                    if newt1 > newt2:
                        #v += ((dist[curP][i] + 1) * (s + flowp))
                        #p(d)
                        #print(f"\tD {v} ({travel1}) ({travele}) {t} {curP} {curE} to {i} {curE} {aux} newt1 {newt1} newt2 {newt2} {s} {v}dis {dist[curP][i]}")
                        v += part2(valves, valvesDic, dist, i, curE, aux, newt1, newt1, newt2,  valves[i].flow,
                                   flowe, vv,d + 1, s + flowp)
                    elif newt1 < newt2 :
                        #v += ((dist[curP][i] + 1) * (s + flowp))
                        #p(d)
                        #print(f"\tE {v} ({travel1}) ({travele}) {t} {curP} {curE} to {i} {curE} {aux} newt1 {newt1} newt2 {newt2} {s} {v}dis {dist[curP][i]}")
                        v += part2(valves, valvesDic, dist, i, curE, aux, newt2, newt1, newt2, valves[i].flow,
                                   flowe, vv,d + 1, s + flowp)
                    else:
                        #v += ((dist[curP][i] + 1) * (s + flowp))
                        #p(d)
                        #print(f"\tF {v} ({travel1}) ({travele}) {t} {curP} {curE} to {i} {curE} {aux} newt1 {newt1} newt2 {newt2} {s} {v} dis {dist[curP][i]}")
                        v += part2(valves, valvesDic, dist, i, curE, aux, newt1, newt1, newt2, valves[i].flow, flowe,vv, d + 1,
                                   s + flowp)
                else:
                    if newt2 > 0:
                        #v = t * (s + flowp)

                        v += part2(valves, valvesDic, dist, curP, curE, aux, newt2, 100000, 0, 0, flowe,vv, d + 1,
                                   s + flowp)
                    else:
                        #v = t * (s + flowp)
                        pass
                    #p(d)
                    #print(f"\t {cur} to {i} {aux} no t {v}")
                """if newt1 > 0 and newt2 > 0:
                    v = ((dist[curP][i] + 1) * s) + ((dist[curE][j] + 1) * s)
                    # p(d)
                    # print(f"\t {cur} to {i} {aux} newt{newt} {s} {v}")
                    v += part2(valves, valvesDic, dist, i, aux, newt1, l, d + 1, s + valves[i].flow, vv)
                else:
                    v = t * s"""
                    #
                if returnMax < v:
                    #p(d)
                    #print(f"! max > {returnMax} {v}")
                    returnMax = v
                vv.pop()
    elif travele == t:
        if len(possible) == 0:
            pass
            #max = ((t) * flowe)#((t+1) * flowe)
            """if travel1 > 0:
                p(d)
                print(f"\tGG {max} to {curP} {curE} {t-travel1} newt{t-travel1} {s}")
                max += + part2(valves, valvesDic, dist, curP, curE, [], t-travel1, 0, travele-travel1,
                                   flowp, 0, vis, d + 1, s + flowe)
            else:
                max = 0
                p(d)
                print(f"\tGG {max} ")"""
        else:
            #elephant
            for indi in range(len(possible)):
                i = possible[indi]

                vv = []
                for a in vis:
                    vv.append(a)
                vv.append(curE)
                aux = []
                for k in possible:
                    if k != i:
                        aux.append(k)
                #vv.append(i)

                newtE = t - dist[curE][i] - 1

                newtP = travel1
                v = 0#(t) * (flowe)#(t+1) * (flowe)
                if newtE > 0:
                    v += newtE * valves[i].flow
                    # p(d)
                    # print(f"\t {cur} to {i} {aux} newt{newt} {s} {v}")
                    if newtE > newtP:
                        #v += ((dist[curE][i] + 1) * (s + flowp))
                        #p(d)
                        #print(f"\tG {v} ({travel1}) ({travele}) {t} {curP} {curE} to {curP} {i} {aux} newt1 {newtP} newt {newtE} {s} {v}  dis E {dist[curE][i]}")
                        v += part2(valves, valvesDic, dist, curP, i, aux, newtE, newtP, newtE, flowp,valves[i].flow,vv,
                                    d + 1, s + flowe)
                    elif newtE < newtP:
                        #v += ((dist[curE][i] + 1) * (s + flowp))
                        #p(d)
                        #print(f"\tH {v} ({travel1}) ({travele}) {t} {curP} {curE} to {curP} {i} {aux} newt1 {newtP} newt {newtE} {s} {v}  dis E {dist[curE][i]} ??? {t - dist[curE][i] - 1}")
                        v += part2(valves, valvesDic, dist, curP, i, aux, newtP,newtP, newtE, flowp, valves[i].flow,vv,
                                   d + 1, s + flowe)
                    else:
                        #v += ((dist[curE][i] + 1) * (s + flowe))
                        #p(d)
                        #print(f"\tH {v} ({travel1}) ({travele}) {t} {curP} {curE} to {curP} {i} {aux} newt1 {newtP} newt {newtE} {s} {v}  dis E {dist[curE][i]}")
                        v += part2(valves, valvesDic, dist, curP, i, aux, newtE, newtP, newtE, flowp, valves[i].flow, vv,d + 1,
                                   s + flowe)
                else:
                    if newtP > 0:
                        #v = t * (s + flowp)
                        v += part2(valves, valvesDic, dist, curP, curE, aux, newtP,  0,10000, flowp, 0,vv, d + 1,
                                   s + flowe)
                    else:
                        pass
                        #v = t * (s + flowp)
                    # p(d)
                    # print(f"\t {cur} to {i} {aux} no t {v}")
                """if newt1 > 0 and newt2 > 0:
                    v = ((dist[curP][i] + 1) * s) + ((dist[curE][j] + 1) * s)
                    # p(d)
                    # print(f"\t {cur} to {i} {aux} newt{newt} {s} {v}")
                    v += part2(valves, valvesDic, dist, i, aux, newt1, l, d + 1, s + valves[i].flow, vv)
                else:
                    v = t * s"""
                #
                if returnMax < v:
                    #p(d)
                    #print(f"! max > {returnMax} : {v}")
                    returnMax = v
                vv.pop()
    #if max == 0:
    #    return t * s
    #p(d)
    #print(f"red {returnMax}")
    return returnMax


def part1(valves,valvesDic,dist,cur,possible,t,vis,d,s,vv):
    #p(d)
    #print(f"> t {t} : in {cur} ({vv} => {vis}) [sum {s}]")
    if t <= 0:
        return 0
    if possible == 0:
        #p(d)
        #print("ret {t*s}")
        return t * s
    max = 0
    for i in possible:
        l = []
        for a in vis:
            l.append(a)
        l.append(cur)
        aux = []
        for j in possible:
            if j != i:
                aux.append(j)
        vv.append((i))

        newt = t-dist[cur][i]-1
        if newt > 0:
            v = (dist[cur][i]+1) * s
            #p(d)
            #print(f"\t {cur} to {i} {aux} newt{newt} {s} {v}")
            v+= part1(valves,valvesDic,dist,i,aux,newt,l,d+1,s + valves[i].flow,vv)
        else :
            v = t * s
            #p(d)
            #print(f"\t {cur} to {i} {aux} no t {v}")
        if max < v:
            max = v
            #p(d)
            #print(f"! max > {max} {vv}")
        vv.pop()
    if max == 0:
        return t * s
    #p(d)
    #print(f"red {max}")
    return max



"""def mm():
    possibleOrders=[]
    useful = []
    for v in range(len(valves)):
        if valves[v].flow > 0:
            useful.append(v)
    possibleOrders.clear()
    if 0 not in useful:
        possibleOrders.append(0)
    for v in range(len(useful)):
        possibleOrders.append(v)

    tovisit = len(useful)
    if 0 in useful:
        tovisit-=1
    global max
    max = 0
    p(useful,valves,dist,valvesDic,30,0,tovisit)
    for i in range(1,len(useful)):
        for j in range(1, len(useful)):
            if(i == j):
                continue
            a = useful[i]
            useful[i] = useful[j]
            useful[j] = a
            v = search(useful,dist,valves,valvesDic)

            a = useful[i]
            useful[i] = useful[j]
            useful[j] = a
            
def p(useful,valves,dist,valvesDic,t,cur,s,total,tovisit):
    if t <= 0:
        return s
    if tovisit == 0:
        global max
        if max < total+(s*t):
            max = total+(s*t)
        return s*t

    for i in useful:
        if useful[i].open == False:
            useful[i].open = True
            subs = s + dist[cur][i]+1
            a = p(useful, valves,dist,valvesDic,t-dist[cur][i]-1,i,s+valves[i].flow,total+subs,tovisit-1)

            useful[i].open = False




def search(useful,dist,valves,valvesDic):
    pass

def m():
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
    pass"""

if __name__ == "__main__":
    main()