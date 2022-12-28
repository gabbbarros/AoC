f = open("input","r")


duplicated = 0
a = []
b = []
overlap = 0
for x in f:
    x = x.replace("\n","")

    aux = x.split(",")

    aux1 = aux[0].split("-")
    a = [int(aux1[0]), int(aux1[1])]
    aux = aux[1].split("-")
    b = [int(aux[0]), int(aux[1])]

    if(a[0] > b[0]) :
        c = a
        a = b
        b = c
    elif a[0] == b[0] and a[1] < b[1]:
        c = a
        a = b
        b = c

    print(f"> a {a} b {b}")

    if a[0] <= b[0] and a[1] >= b[1]:
        duplicated+=1
        #print("added")

    if a[0] <= b[0] and a[0] <= b[1] and a[1] >= b[0]:
        overlap+=1
        print("added")


print(duplicated)
print(overlap)