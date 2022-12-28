f = open("sminput", "r")

sum=0
max = [0,0,0]
for x in f:
  if x == "\n" :
    if sum > max[0] :
      max[0] = sum
      max.sort()
    sum = 0
  else:
    sum += int(x)

if sum > max[0]:
  max[0] = sum

t = max[0]+max[1]+max[2]
print(t)
