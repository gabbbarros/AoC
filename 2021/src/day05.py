f = open("sminput","r")

def in_print(lines,quant):
    out = []
    largStack = 0
    for z in range(quant):
        if len(lines[z]) > largStack:
            largStack = len(lines[z])

    for y in range(largStack).__reversed__():
        s = []
        for z in range(quant):
            if(len(lines[z]) > y):
                s.append((lines[z][y]))
            else:
                s.append(" ")
        out.append(s)

    for z in out:
        for y in z:
            print(f"{y}\t", end="")
        print("")

lines = []

inp = []
started = False
for x in f:
    x = x.replace("\n","")

    if not started:
        if len(x) == 0:
            print(inp)
            started = True
            for y in inp[len(inp)-1]:
                s = inp[len(inp)-1]

            s = s.split(" ")
            quant = int(s[len(s)-1])

            for y in range(quant):
                lines.append([])

            y = len(inp)-2
            while y >= 0:
                z = 1
                st = 0
                while z < len(inp[y]):
                    if inp[y][z] != " ":
                        lines[st].append(inp[y][z])
                    else:
                        pass
                    z+=4
                    st+=1
                y-=1


            in_print(lines,quant)
            print(inp)
            inp.clear()
            #stop initial config
        else:
            inp.append(x)
    else:
        #move 1 from 2 to 1
        x = x.split(" ")
        q = int(x[1])
        fro = int(x[3])-1
        to = int(x[5])-1
        mid = []
        i = len(lines[fro]) - q
        #in_print(lines,quant)
        while i < len(lines[fro]) :
            lines[to].append(lines[fro][i])
            i+=1

        while q > 0 :
            lines[fro].pop()
            q-=1
print("-----------")
in_print(lines,quant)

out = ""
for i in range(quant):
    out += (lines[i].pop())
print(out)
