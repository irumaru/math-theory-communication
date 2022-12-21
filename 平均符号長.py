p = [2/16, 3/16, 6/16, 1/16, 4/16]
s = [4, 3, 1, 4, 2]

total = 0
for i in range(0,len(s)):
    total += p[i]*s[i]

print(total)