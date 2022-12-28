f = open("input", "r")

op= {"A":0,"B":1,"C":2}
pl= {"X":0,"Y":1,"Z":2}
piece = [1,2,3]
def part1(s) :
    score = pl[s[1]] + 1
    dif = pl[s[1]] - op[s[0]]
    if (dif == 1 or dif == -2):
        score += 6
    elif (dif == 0):
        score += 3
    return score


def part2(s):
    score = 0
    if(s[1] == "Z"):#win
        choice = (op[s[0]] + 1) % 3
        score = 6 + piece[choice]
    elif(s[1] == "Y"):#draw
        choice = op[s[0]]
        score = 3 + piece[choice]
    else:
        choice = (op[s[0]] + 2 ) % 3
        score = piece[choice]
    return score

score1 = 0
score2 = 0
for x in f:
    s = x.replace("\n","").split(" ")
    score1 += part1(s)
    score2 += part2(s)

print(score1)
print(score2)
