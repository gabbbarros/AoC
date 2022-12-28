
def turn_to_list(x):
    n1 = []
    #print(x)
    for a in x:
        if len(a) > 0:
            #print(f".{a}.")
            n1.append(int(a))
    r,_ = package(n1,1)
    #print(f">> R {r}")

        #print(f"\t{a} : {n1}")
    return r

def package(og,index):
    r = []
    while index < len(og):
        if og[index] == -1:
            new, ind = package(og,index+1)
            r.append(new)
            index = ind
        elif og[index] == -2:
            return r,index
        else:
            r.append(og[index])
        index+=1
    return r,index


def check(p1, p2, internal = True) :
    print(f"\t{p1}\n\t{p2} {len(p1)} {len(p2)}")
    print(f"? {len(p1)} {p1} {len(p2)} {p2}")
    """if internal and len(p2) < len(p1):
        print("5")
        return False"""
    size = len(p1) if len(p1) < len(p2) else len(p2)

    #for i in range(size):
    i = 0
    comp1 = False
    while i < len(p1):
        if i == len(p2):
            print("6")
            return -1
        #if i >= len(p2):
            #print(f"i {i} {len(p1)} {p1} {len(p2)} {p2}")
            #print(5)
            #return False
        if type(p1[i]) == type(p2[i]):
            if type(p1[i]) == int:
                print(f"0 {p1[i]} {p2[i]}")
                if p1[i] > p2[i]:
                    print("0F")
                    return -1
                elif p1[i] < p2[i]:
                    print("0T")
                    return 1

                comp1 = True
            else:
                print(f"1")
                b = check(p1[i],p2[i])
                if b != 0:
                    print(f"11")
                    return b
        elif type(p1[i]) == int:
            print("2")
            b = check([p1[i]], p2[i], False)
            if b != 0:
                print("22")
                return b
        else:
            print("3")
            b = check(p1[i], [p2[i]], False)
            if b != 0:
                print("33")
                return b
        i+=1

    if i == len(p1) and  i != len(p2):
        return 1

    return 0

def main():
    packets = []
    pair = 1
    rightOrder = 0
    with open("sminput","r") as f:
        for x in f:
            if len(x) <= 1:
                continue
            x = x.strip()
            print(x)
            x = x.replace("[",",-1,").replace("]",",-2,").split(",")
            n1 = turn_to_list(x)
            packets.append(n1)

    i = 0
    while i < len(packets):
        in_order = check(packets[i],packets[i+1],False)
        if in_order != -1:
            rightOrder+=pair
        print(f"Pair {pair} : {in_order}")
        pair+=1
        #exit()
        print("----")
        i+=2
    print(f"Part 1 {rightOrder}")

    deco = [[[2]],[[6]]]
    packets.append(deco[0])
    packets.append(deco[1])
    modified = True
    while modified:
        modified = False

        i = 0
        while i < len(packets)-1:
            in_order = check(packets[i], packets[i + 1], False)
            if in_order < 0:
                modified = True
                aux = packets[i]
                packets[i] = packets[i+1]
                packets[i+1] = aux
            i+=1

    index = 1
    i = 1
    list = []
    for a in packets:
        if a in deco:
            index *= i
            list.append(i)
        print(a)
        i+=1
    print(f"Part 2 {index} ??{list}")





if __name__ == "__main__":
    main()