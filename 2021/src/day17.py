
def main():
    input = None
    with open("../input/day17.txt","r") as f:
        for x in f:
            input = [1 if a == ">" else -1 for a in x]

    print(input)

    h = 2022*4
    w = 7

    #print(f"Part 1: {part1(w, h, input)}")
    part2(w, h, input)


def part2(w, h, input):
    h = 100000 * 4
    wall = [[0 for a in range(w)] for b in range(h)]
    print(len(wall))
    print(len(wall[0]))
    order = ["-", "+", "L", "|", "o"]

    x0 = 2
    y0 = h - 4
    jet = 0
    piece = 0
    DEBUG = False
    for it in range(1,100000):
        xb = x0
        yb = y0

        stopped = False
        if DEBUG:
            print(f"\t-------------------- {it} Created {order[piece]} {x0}, {y0}")

            print_midway(wall,order[piece],xb,yb,w,h)

        while not stopped:

            if DEBUG:
                print(f"H {jet} : {input[jet]}")
            #horizontal
            if input[jet] == -1:
                #left
                if can_move_left(wall, order[piece], xb, yb):
                    xb -= 1
            else:
                #right
                if can_move_right(wall, order[piece], xb, yb, w):
                    xb += 1

            if DEBUG:
                print_midway(wall, order[piece], xb, yb, w, h)
                print("Down")
            #vertical
            if can_move_down(wall, order[piece], xb, yb, h):
                yb+=1
            else:
                n = stick_piece(wall, order[piece], xb, yb)
                if n < y0:

                    if DEBUG:
                        print(f"\tupdating {y0} > {n}")
                    y0 = n
                else:
                    if DEBUG:
                        print(f"\tBAD RETURN {y0} > {n}")
                stopped = True

            jet += 1
            if jet >= len(input):
                jet = 0
            #y0 = talles - 4
            if DEBUG:
                print_midway(wall,order[piece],xb,yb,w,h)
                print("----")
                print(f"y0 {y0} y0 + 3 {y0 + 3} h - y0 {h - y0} h - y0 + 3 {h - y0 + 3} h - y0 - 3 {h - y0 - 4}")

        piece += 1
        if piece >= len(order):
            piece = 0

    """for y in range(h-10,h):
        for x in range(w):
            print(wall[y][x],end="")
        print("")"""
    piece -=1
    if piece < 0:
        piece = 0
    print_final(wall, order[piece], xb, yb, w, h, no_bottom = False)
    print(f"height:{y0-4}   -> {h-1}")
    found = False
    for height in range(30, 3000):
        for yb in range(h-4000, h).__reversed__():
            patbot = yb
            pattop = yb - height

            #print(f"\t??? h: {h} yb: {yb} {patbot} {pattop}")
            bad = False
            for yy in range(pattop, patbot+1):
                for xx in range(0, w):
                    if wall[yy][xx] != wall[yy-height-1][xx]:# or wall[yy][xx] != wall[yy-(height*2)-2][xx]:
                            #print(f"\tBad {wall[yy]} !" )
                            bad = True
                            break
                if bad:
                    break

            if not bad:
                found = True
                print(f"found {patbot} {pattop}")
                break
        if found:
            break
    print(f" found? {found}")
    if found:
        c = 0
        i = 0
        for yy in range(pattop, patbot + 1):
            print(i,"\t")
            print(wall[yy])
            i+=1
        i = 0
        last_piece=0

        top = [[wall[ay][ax] for ax in range(w)] for ay in range(pattop, pattop+6)]

        init = [[0 for ax in range(w)] for ay in range(5)]
        for yy in range(pattop, patbot + 1).__reversed__():
            #print(i,end="\t")
            i+=1
            #print(wall[yy])
            for xx in range(0,w):
                if wall[yy][xx] == "|":
                    c += 1
                    wall[yy][xx] = 1
                    wall[yy-1][xx] = 1
                    wall[yy-2][xx] = 1
                    wall[yy-3][xx] = 1
                    if(yy - 3 < pattop):
                        dif = pattop - yy
                        for ay in range(dif+1):
                            init[5-1-ay][xx]=1
                    last_piece = 3
                elif wall[yy][xx] == "-":
                    c += 1
                    wall[yy][xx] = 2
                    wall[yy][xx + 1] = 2
                    wall[yy][xx + 2] = 2
                    wall[yy][xx + 3] = 2
                    last_piece = 0
                elif wall[yy][xx] == "+":
                    c += 1

                    wall[yy][xx] = 3
                    wall[yy - 1][xx] = 3
                    wall[yy - 2][xx] = 3
                    wall[yy - 1][xx - 1] = 3
                    wall[yy - 1][xx + 1] = 3
                    if yy - 1 < pattop:
                        init[4][xx] = 1
                        init[4][xx - 1] = 1
                        init[4][xx + 1] = 1
                        init[3][xx] = 1
                    elif (yy - 2 < pattop):
                        init[4][xx] = 1
                    last_piece = 1
                elif wall[yy][xx] == "L":
                    if wall[yy][xx] == "L":
                        c += 1
                        wall[yy][xx] = 4
                        if wall[yy - 1][xx + 2] == "L":
                            wall[yy - 1][xx + 2] = 4
                        if wall[yy - 2][xx + 2] == "L":
                            wall[yy - 2][xx + 2] = 4
                        wall[yy][xx + 1] = 4
                        wall[yy][xx + 2] = 4
                        if yy - 1 < pattop:
                            init[3][xx + 2] = 1
                            init[4][xx + 2] = 1
                        elif (yy - 2 < pattop):
                            init[4][xx + 2] = 1
                    else:
                        wall[yy][xx] = 4
                        if wall[yy - 1][xx + 2] == "L":
                            wall[yy - 1][xx + 2] = 4
                        if wall[yy - 2][xx + 2] == "L":
                            wall[yy - 2][xx + 2] = 4
                        if yy - 1 < pattop:
                            init[3][xx + 2] = 1
                            init[4][xx + 2] = 1
                        elif (yy - 2 < pattop):
                            init[4][xx + 2] = 1
                    last_piece = 2
                elif wall[yy][xx] == "x":
                    c += 1
                    wall[yy][xx] = 5
                    wall[yy - 1][xx] = 5
                    wall[yy][xx + 1] = 5
                    wall[yy - 1][xx + 1] = 5
                    if yy - 1 < pattop:
                        init[4][xx + 1] = 1
                        init[4][xx] = 1
                    last_piece = 4

        pieces_below = h-patbot - 1
        print(f"pieces :{c} patbot {patbot} pieces below: {pieces_below}")

        remains = 1000000000000 - pieces_below
        print(int(remains/c))
        above_loop = 1000000000000 - pieces_below - (c*int(remains/c))
        print(above_loop)
        height_in_loop = int(remains/c) * (patbot - pattop+1)
        new_c = 0
        ab_height = 0
        i = 0
        for yy in range(pattop, patbot + 1).__reversed__():
            #print(i, end="\t")
            i += 1
            #print(wall[yy])
            for xx in range(0,w):
                if wall[yy][xx] == 1:
                    new_c += 1
                    wall[yy][xx] = 0
                    wall[yy-1][xx] = 0
                    wall[yy-2][xx] = 0
                    wall[yy-3][xx] = 0
                elif wall[yy][xx] == 2:
                    new_c += 1
                    #print(wall[yy])
                    #print(f"{yy} {xx}")
                    wall[yy][xx] = 0
                    wall[yy][xx + 1] = 0
                    wall[yy][xx + 2] = 0
                    wall[yy][xx + 3] = 0

                elif wall[yy][xx] == 3:
                    new_c += 1
                    wall[yy][xx] = 0
                    wall[yy - 1][xx] = 0
                    wall[yy - 2][xx] = 0
                    wall[yy - 1][xx - 1] = 0
                    wall[yy - 1][xx + 1] = 0
                elif wall[yy][xx] == 4:
                    if wall[yy][xx+1]==4:
                        new_c += 1
                        wall[yy][xx] = 0
                        if wall[yy - 1][xx + 2] == 4:
                            wall[yy - 1][xx + 2] = 0
                        if wall[yy - 2][xx + 2] == 4:
                            wall[yy - 2][xx + 2] = 0
                        wall[yy][xx + 1] = 0
                        wall[yy][xx + 2] = 0
                    else:
                        wall[yy][xx] = 0
                        if wall[yy - 1][xx + 2] == 4:
                            wall[yy - 1][xx + 2] = 0
                        if wall[yy - 2][xx + 2] == 4:
                            wall[yy - 2][xx + 2] = 0
                elif wall[yy][xx] == 5:
                    new_c += 1
                    wall[yy][xx] = 0
                    wall[yy - 1][xx] = 0
                    wall[yy][xx + 1] = 0
                    wall[yy - 1][xx + 1] = 0
                #print(f"\tab {above_loop} {new_c}")
                if above_loop == new_c:
                    ab_height = yy
                    break

            if ab_height > 0:
                break

        auxTop = [top[ay] for ay in range(len(top))]
        initial_jet, last_piece = find_last_piece_and_jet(w, h, input, 100000, pattop, top)
        initial_piece = last_piece+1
        if initial_piece >= len(order):
            initial_piece = 0
        print(f"init {initial_piece}\n{init}")
        quantRepeated = int((1000000000000-pieces_below)/c)
        part = part1(w,h,input,above_loop+pieces_below+1,init, initial_piece,initial_jet)
        print(f"init {initial_piece}\n{init}")
        print(part)
        print(f"answer: {part+height_in_loop}")
        print(f"hi mid: {patbot-pattop} {patbot} {pattop} {h}")
        print(f"{int(remains/c)} {(patbot - pattop+1)} height_in_loop = int(remains/c) * (patbot - pattop+1) {c} {1000000000000-c}")
        print(f">>> {height_in_loop} + {pieces_below} + {h-ab_height} = {height_in_loop +pieces_below+ab_height} ({height_in_loop +pieces_below})")


    print(f"y0 {y0} y0 + 3 {y0 + 3} h - y0 {h - y0} h - y0 + 3 {h - y0 + 3} h - y0 - 3 {h - y0 - 4}")




    return h - y0 - 4

def find_last_piece_and_jet(w, h, input, quant = 100000, max_height = 10, top = []):
    wall = [[0 for a in range(w)] for b in range(h)]

    print(len(wall))
    print(len(wall[0]))
    order = ["-", "+", "L", "|", "o"]

    x0 = 2
    y0 = h - 4

    jet = 0
    piece = 0

    DEBUG = False

    for it in range(1,quant):
        xb = x0
        yb = y0

        stopped = False
        if DEBUG:
            print(f"\t-------------------- {it} Created {order[piece]}")
            print_midway(wall,order[piece],xb,yb,w,h)

        while not stopped:

            if DEBUG:
                print(f"H {jet} : {input[jet]}")
            #horizontal
            if input[jet] == -1:
                #left
                if can_move_left(wall, order[piece], xb, yb):
                    xb -= 1
            else:
                #right
                if can_move_right(wall, order[piece], xb, yb, w):
                    xb += 1

            if DEBUG:
                print_midway(wall, order[piece], xb, yb, w, h)
                print("Down")
            #vertical
            if can_move_down(wall, order[piece], xb, yb, h):
                yb+=1
            else:
                n = stick_piece(wall, order[piece], xb, yb)
                if n < y0:

                    if DEBUG:
                        print(f"\tupdating {y0} > {n}")
                    y0 = n
                else:
                    if DEBUG:
                        print(f"\tBAD RETURN {y0} > {n}")
                stopped = True

            jet += 1
            if jet >= len(input):
                jet = 0
            #y0 = talles - 4
            if DEBUG:
                print_midway(wall,order[piece],xb,yb,w,h)
                print("----")
                print(f"y0 {y0} y0 + 3 {y0 + 3} h - y0 {h - y0} h - y0 + 3 {h - y0 + 3} h - y0 - 3 {h - y0 - 4}")

        if y0 + 3 <= max_height:
            equal = True
            for ay in range(len(top)):
                print(top[ay])
            print("?")
            for ay in range(max_height, max_height + len(top)):
                print(wall[ay])
            for ay in range(max_height,max_height+len(top)):

                print(f"{len(top)} {ay} {ay-max_height}")
                for ax in range(w):
                    if wall[ay][ax] != top[ay-max_height][ax]:
                        equal = False
                        break
                if not equal:
                    break
            if equal:
                return jet, piece


        piece += 1
        if piece >= len(order):
            piece = 0


    return h - y0 - 4

def part1(w, h, input, quant = 2023, init = None, initial_piece = None, initial_jet = None, find_jet = False, last_piece = None, max_height = None):
    wall = [[0 for a in range(w)] for b in range(h)]

    print(len(wall))
    print(len(wall[0]))
    order = ["-", "+", "L", "|", "o"]

    x0 = 2
    y0 = h - 4

    if init is not None:
        for y in range(len(init)):
            for x in range(len(init[0])):
                wall[h-(len(init) - y)][x] = init[y][x]
                if init[y][x] == 1 :
                    if h-(len(init) - y) - 3 < y0:
                        y0 = h-(len(init) - y) - 4
                        print(f"here {y0}")

        for y in range(h - len(init) - 5, h):
            print(wall[y])


    jet = 0
    piece = 0
    if initial_piece is not None:
        piece = initial_piece

    if initial_jet is not None:
        jet = initial_jet




    DEBUG = False


    for it in range(1,quant):
        xb = x0
        yb = y0

        stopped = False
        if DEBUG:
            print(f"\t-------------------- {it} Created {order[piece]}")

            print_midway(wall,order[piece],xb,yb,w,h)

        while not stopped:

            if DEBUG:
                print(f"H {jet} : {input[jet]}")
            #horizontal
            if input[jet] == -1:
                #left
                if can_move_left(wall, order[piece], xb, yb):
                    xb -= 1
            else:
                #right
                if can_move_right(wall, order[piece], xb, yb, w):
                    xb += 1

            if DEBUG:
                print_midway(wall, order[piece], xb, yb, w, h)
                print("Down")
            #vertical
            if can_move_down(wall, order[piece], xb, yb, h):
                yb+=1
            else:
                n = stick_piece(wall, order[piece], xb, yb)
                if n < y0:

                    if DEBUG:
                        print(f"\tupdating {y0} > {n}")
                    y0 = n
                else:
                    if DEBUG:
                        print(f"\tBAD RETURN {y0} > {n}")
                stopped = True

            jet += 1
            if jet >= len(input):
                jet = 0
            #y0 = talles - 4
            if DEBUG:
                print_midway(wall,order[piece],xb,yb,w,h)
                print("----")
                print(f"y0 {y0} y0 + 3 {y0 + 3} h - y0 {h - y0} h - y0 + 3 {h - y0 + 3} h - y0 - 3 {h - y0 - 4}")

        piece += 1
        if piece >= len(order):
            piece = 0

        #if it == 50:
        #    print_final(wall, order[piece], xb, yb, w, h, no_bottom=False)
        #    exit()
    """for y in range(h-10,h):
        for x in range(w):
            print(wall[y][x],end="")
        print("")"""
    piece -=1
    if piece < 0:
        piece = 0
    print_final(wall, order[piece], xb, yb, w, h, no_bottom = False)
    print(f"y0 {y0} y0 + 3 {y0 + 3} h - y0 {h - y0} h - y0 + 3 {h - y0 + 3} h - y0 - 3 {h - y0 - 4}")

    return h - y0 - 4


def can_move_left(wall, piece, xb, yb):
    if piece == "-":
        if xb > 0 and wall[yb][xb - 1] == 0:
            return True
    elif piece == "+":
        if xb > 0 and wall[yb][xb] == 0 and wall[yb-1][xb-1] == 0 and wall[yb-2][xb] == 0:
            return True
    elif piece == "L":
        if xb > 0 and wall[yb][xb - 1] == 0 and wall[yb-1][xb+1] == 0 and wall[yb-2][xb+1] == 0:
            return True
    elif piece == "|":
        if xb > 0:
            for a in range(yb-3, yb+1):
                if wall[a][xb - 1] != 0:
                    return False
            return True
    elif piece == "o":
        if xb > 0 and wall[yb][xb - 1] == 0 and wall[yb - 1][xb - 1] == 0:
            return True
    return False

def can_move_right(wall, piece, xb, yb, w):
    if piece == "-":
        if xb+4 < w and wall[yb][xb + 4] == 0:
            return True
    elif piece == "+":
        if xb+3 < w and wall[yb][xb + 2] == 0 and wall[yb-1][xb+3] == 0 and wall[yb-2][xb+2] == 0:
            return True
    elif piece == "L":
        if xb+3 < w and wall[yb][xb + 3] == 0 and wall[yb-1][xb+3] == 0 and wall[yb-2][xb+3] == 0:
            return True
    elif piece == "|":
        if xb+1 < w:
            for a in range(yb-3,yb+1):
                if wall[a][xb + 1] != 0:
                    return False
            return True
    elif piece == "o":
        if xb + 2 < w and wall[yb][xb + 2] == 0 and wall[yb - 1][xb + 2] == 0:
            return True
    return False

def can_move_down(wall, piece, xb, yb, h):
    if piece == "-":
        if yb + 1 < h:
            for a in range(xb, xb+4):
                if wall[yb + 1][a] != 0:
                    return False
            return True
    elif piece == "+":
        if yb + 1 < h and wall[yb+1][xb+1] == 0 and wall[yb][xb] == 0 and wall[yb][xb+2] == 0:
            return True
    elif piece == "L":
        if yb+1 < h and wall[yb+1][xb] == 0 and wall[yb+1][xb+1] == 0 and wall[yb+1][xb+2] == 0:
            return True
    if piece == "|":
        if yb + 1 < h and wall[yb + 1][xb] == 0:
            return True
    elif piece == "o":
        if yb+1 < h and wall[yb + 1][xb] == 0 and wall[yb + 1][xb + 1] == 0:
            return True
    return False

def stick_piece(wall, piece, xb, yb):
    wa = "#"
    if piece == "-":
        wa = "-"
        for a in range(xb,xb+4):
            wall[yb][a] = wa
        return yb-1-3
    elif piece == "+":
        wa = "+"
        wall[yb - 1][xb] = wa
        wall[yb - 1][xb + 1] = wa
        wall[yb - 1][xb + 2] = wa
        wall[yb - 2][xb + 1] = wa
        wall[yb][xb + 1] = wa
        return yb - 3 - 3
    elif piece == "L":
        wa = "L"
        wall[yb][xb] = wa
        wall[yb][xb + 1] = wa
        wall[yb][xb + 2] = wa
        wall[yb - 1][xb + 2] = wa
        wall[yb - 2][xb + 2] = wa
        return yb - 3 - 3
    elif piece == "|":
        wa = "|"
        for a in range(yb-3,yb+1):
            wall[a][xb] = wa
        return yb-4-3
    elif piece == "o":
        wa = "x"
        wall[yb][xb] = wa
        wall[yb][xb + 1] = wa
        wall[yb - 1][xb] = wa
        wall[yb - 1][xb + 1] = wa
        return yb - 2 - 3

    return yb

def print_midway(wall, piece, xb, yb, w, h, no_bottom = True):
    print(piece)
    if no_bottom:
        end = yb + 10
        if end > h:
            end = h
    else:
        end = h
    for y in range(yb - 5, end):
        for x in range(w):
            if piece == "-":
                if x >= xb and x <= xb + 3 and y == yb:
                    print("-", end="")
                else:
                    print(wall[y][x], end="")
            elif piece == "+":
                if y == yb-1 and (x == xb or x == xb + 1 or x == xb + 2):
                    print("+", end="")
                elif y == yb and xb+1 == x:
                    print("+", end="")
                elif y == yb - 2 and x == xb+1:
                    print("+", end="")
                else:
                    print(wall[y][x], end="")
            elif piece == "L":
                if (xb <= x <= xb + 2 and y == yb) or (x == xb+2 and yb - 2 <= y < yb):
                    print("L", end="")
                else:
                    print(wall[y][x], end="")
            elif piece == "|":
                if yb - 3 <= y <= yb and x == xb:
                    print("|", end="")
                else:
                    print(wall[y][x], end="")
            elif piece == "o":
                if (y == yb - 1 or y == yb) and (x == xb or x == xb + 1):
                    print("o", end="")
                else:
                    print(wall[y][x], end="")
            else:
                print(wall[y][x], end="")
        print("")
    print("----")

def print_final(wall, piece, xb, yb, w, h, no_bottom = True):
    print(piece)
    if no_bottom:
        end = yb + 10
        if end > h:
            end = h
    else:
        end = h
    for y in range(yb - 5, end):
        for x in range(w):
            if wall[y][x] == 0:
                print(" ", end="")
            else:
                print(wall[y][x], end="")
        print("")
    print("----")

if __name__ == "__main__":
    main()