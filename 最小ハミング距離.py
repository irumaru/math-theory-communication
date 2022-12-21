ss = ['0000', '0011', '0101', '0110']
ss += ['1001', '1010', '1100', '1111']

for i in range(0, len(ss)):
    ss[i] = list(ss[i])

hmin = len(ss)
count = 0
for ns1 in range(0, len(ss)):
    for ns2 in range(ns1 + 1, len(ss)):
        h = 0
        print('比較: ' + str(ss[ns1]) + ' XOR ' + str(ss[ns2]))
        for i in range(0, len(ss[ns1])):
            if(ss[ns1][i] != ss[ns2][i]):
                h += 1
        print('ハミング距離: ' + str(h))
        if(h < hmin):
            hmin = h
        count += 1

print('計算量: ' + str(count) + '  最小ハミング距離: ' + str(hmin))