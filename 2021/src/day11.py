
def read_input():
    monkeys = []
    z = 1
    with open("sminput","r") as f:
        length = len("  Starting items: ")
        for x in f:
            x = x.strip()
            if x.startswith("Monkey"):
                m = [[],[]]
                x = f.readline()[length:].split(", ")
                for a in x:
                    m[0].append(int(a))
                x = f.readline().strip().split("= ")[1].split(" ")
                for a in x:
                    if a.isdigit():
                        m[1].append(int(a))
                    else:
                        m[1].append(a)
                x = f.readline().strip().split("by ")
                m.append(int(x[1]))
                z *= int(x[1])
                x = f.readline().strip().split(" ")
                m.append(int(x[len(x)-1]))
                x = f.readline().strip().split(" ")
                m.append(int(x[len(x)-1]))
                print(m)
                monkeys.append(m)
    return monkeys,z

def operate(a,b,op):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b

def part1(monkeys,z,time,part):
    dic = {}
    for i in range(len(monkeys)):
        dic[i] = 0

    for i in range(time):
        for j in range(len(monkeys)):
            m = monkeys[j]
            for x in range(len(m[0])):
                if m[1][len(m[1]) - 1] == "old":
                    m[0][x] = operate(m[0][x], m[0][x], m[1][1])
                else:
                    m[0][x] = operate(m[0][x], m[1][len(m[1]) - 1], m[1][1])

                if part == 1:
                    m[0][x] = int(m[0][x]/3)
                else:
                    m[0][x] = m[0][x] % z
                if m[0][x] % m[2] == 0:
                    monkeys[m[3]][0].append(m[0][x])
                else:
                    monkeys[m[4]][0].append(m[0][x])

                dic[j] = dic[j] + 1
            m[0].clear()
        #print(dic)

    print("---")
    for m in monkeys:
        print(m)
    print(dic)

    a = [0, 0]
    for v in dic.values():
        if v > a[0]:
            a[0] = v
            a.sort()
    print(a[0] * a[1])

def part2(monkeys,z):
    dic = {}
    for i in range(len(monkeys)):
        dic[i] = 0

    for i in range(10000):
        for j in range(len(monkeys)):
            m = monkeys[j]
            for x in range(len(m[0])):
                if m[1][len(m[1]) - 1] == "old":
                    m[0][x] = operate(m[0][x], m[0][x], m[1][1])
                else:
                    m[0][x] = operate(m[0][x], m[1][len(m[1]) - 1], m[1][1])

                # only for part 1
                # m[0][x] = int(m[0][x]/3)
                m[0][x] = m[0][x] % z
                if m[0][x] % m[2] == 0:
                    monkeys[m[3]][0].append(m[0][x])
                else:
                    monkeys[m[4]][0].append(m[0][x])

                dic[j] = dic[j] + 1
            m[0].clear()
            # print(m)

            #print(f">{i}: m {j} {m}")
        #print(dic)

    print("---")
    for m in monkeys:
        print(m)
    print(dic)

    a = [0, 0]
    for v in dic.values():
        if v > a[0]:
            a[0] = v
            a.sort()
    print(a[0] * a[1])

def copy_monks(monkeys):
    babies = []
    for i in range(len(monkeys)):
        m = monkeys[i]
        b = []
        for j in range(len(m)):
            a = m[j]
            if type(a) is int:
                b.append(a)
            else:
                l = []
                for k in m[j]:
                    l.append(k)
                b.append(l)

        babies.append(b)
    return babies


def main():
    monkeys,z = read_input()
    part1(copy_monks(monkeys),z,20,1)
    part1(monkeys, z, 10000, 2)

    """monkeys,z = read_input()
    print("######")
    part2(monkeys.copy(),z)"""







if __name__ == "__main__":
    main();