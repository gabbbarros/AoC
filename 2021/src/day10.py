
def main():
    r = 1
    prev = 0
    i = 1
    sum = 0
    st = []
    cycles = [20,60,100,140,180,220]
    with open("sminput","r") as f:
        for x in f:
            x = x.strip().split(" ")
            if x[0] == "addx":
                t = 2
            else:
                t = 1
            while t > 0:
                if i in cycles:
                    strength = i * r
                    sum += strength
                    st.append([strength])

                draw = (i-1) % 40
                if draw==0:
                    print("")
                if r-1 <= draw and r+1 >= draw:
                    print("#",end="")
                else:
                    print(".", end="")

                if t == 1:
                    r += prev
                    prev = 0

                if x[0] == "addx" and t == 2:
                    prev = int(x[1])

                t -= 1
                i+=1


    print(f"\nPart 1: {sum}")

if __name__ == "__main__":
    main()