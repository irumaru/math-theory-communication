import math

xs = [1/2, 1/4, 1/2]
ys = [1/2, 1/2]

total = 0

for y in ys:
    for x in xs:
        i = - math.log2(x)
        total += y * i * x

print(total)