import math

ps = [0.3, 0.25, 0.2, 0.1, 0.1, 0.05]

total = 0

for p in ps:
    i = - math.log2(p)
    total += i * p

print(total)