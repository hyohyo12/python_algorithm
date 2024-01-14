import sys
a=[]
allBreak=True
for i in range(9):
    a.append(int(sys.stdin.readline()))
sum_a = sum(a)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i == j:
            continue
        else:
            if sum_a-(a[i]+a[j]) == 100:
                tmp = a[j]
                a.pop(i)
                a.remove(tmp)
                allBreak = False
                break
    if allBreak == False:
        break
a.sort()
for i in a:
    print(i)