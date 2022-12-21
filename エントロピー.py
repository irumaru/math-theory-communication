import math

#ps = [2/16, 3/16, 6/16, 1/16, 4/16]
ps = [0.125, 1-0.125]

total = 0

for p in ps:
    i = - math.log2(p)
    total += i * p

print(total)