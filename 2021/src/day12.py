import math
import sys
from queue import PriorityQueue

euclid = lambda x0,y0,x1,y1 : math.sqrt(math.pow((x1-x0),2)+math.pow((y1-y0),2))

def swap(a,b):
    return b,a


def h(x0,y0):
    global bestA
    return bestA[(x0,y0)][0]


def canGo(x0, y0, x1, y1, board, node, findEnd):
    if (findEnd and board[y1][x1] <= board[y0][x0] + 1) or (not findEnd and board[y1][x1] >= board[y0][x0] - 1):
        return (h(x1, y1) + node[2] + 1, (x1, y1), node[2] + 1)
    else:
        return None


def main(findEnd = True):
    board=[]
    x0 = 0
    y0 = 0
    yz = 0
    xz = 0
    x = 0
    y = 0
    with open("sminput") as f:
        for ff in f:
            ff = ff.strip()
            l = []
            for x in range(len(ff)):
                if ff[x] == "S":
                    x0 = x
                    y0 = len(board)
                    l.append(ord("a"))
                elif ff[x] == "E":
                    xz = x
                    yz = len(board)
                    l.append(ord("z"))
                else:
                    l.append(ord(ff[x]))
            board.append(l)

    if not findEnd:
        x0, xz = swap(x0, xz)
        y0, yz = swap(y0, yz)

    visited = set()
    frontier = PriorityQueue()

    frontier.put((0, (x0, y0), 0))
    result = None

    global bestA
    if findEnd:
        bestA = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                p = None
                small = euclid(j, i, xz, yz)
                bestA[(j, i)] = (small, p)
    else:
        allAs = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ord("a"):
                    allAs.append((j,i))

        bestA = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                small = sys.maxsize
                p = None
                for a in allAs:
                    c = euclid(j, i, a[0], a[1])
                    if c < small:
                        small = c
                        p = a
                bestA[(j, i)] = (small, p)

        allAs.clear()
        del allAs

    dir = [(0,-1),(0,1),(-1,0),(1,0)]
    while not frontier.empty():
        node = frontier.get()

        if node[1] in visited:
            continue
        visited.add(node[1])

        x = node[1][0]
        y = node[1][1]
        if (findEnd and x == xz and y == yz) or (not findEnd and board[y][x] == ord("a")):
            result = node
            break;

        for d in dir:
            newx = x+d[0]
            newy = y+d[1]
            if newx >=0 and newx < len(board[0]) and newy >= 0 and newy < len(board):
                n = canGo(x, y, newx, newy, board, node, findEnd)
                if n is not None:
                    frontier.put(n)

    del board
    del visited
    del frontier
    del bestA
    return result[2]

if __name__ == "__main__":
    print(f"Part 1 {main()}")

    print(f"Part 2 {main(False)}")