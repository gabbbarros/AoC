f = open("input", "r")

def CreateDic(x, size):
    count = {}

    i = 0
    while i < size:
        count[x[i]] = 1
        i += 1
    return count

def Part1(x):
    sum = 0
    count = CreateDic(x, int(len(x)/2))
    i = int(len(x)/2)

    duplicate = set()
    while i < len(x):
        if x[i] in count:
            duplicate.add(x[i])
        i += 1

    for a in duplicate:
        if (a.islower()):
            sum += ord(a) - 96
        else:
            sum += ord(a) - 38
    return sum

def Part2(x,y,z):
    sum = 0
    count = CreateDic(x,len(x))
    duplicate1 = {}
    for i in range(len(y)):
        if y[i]  in count:
            duplicate1[y[i]] = 1

    duplicate2 = set()
    for i in range(len(z)):
        if z[i]  in duplicate1:
            duplicate2.add(z[i])

    for a in duplicate2:
        if (a.islower()):
            sum += ord(a) - 96
        else:
            sum += ord(a) - 38
    return sum

#A 65 a 97 Z 90
sum1 = 0
sum2 = 0
gCount=0
last3 = []
for x in f:
    x = x.replace("\n","")
    sum1 += Part1(x)
    gCount+=1
    last3.append(x);
    if gCount == 3:
        gCount = 0
        sum2 += Part2(last3[0],last3[1],last3[2])

        last3.clear()


print(f"Part 1: {sum1}")
print(f"Part 2: {sum2}")