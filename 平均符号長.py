p = [0.3, 0.25, 0.2, 0.1, 0.1, 0.05]
s = [2, 2, 2, 3, 4, 4]

total = 0
for i in range(0,len(s)):
    total += p[i]*s[i]

print(2.37/total)