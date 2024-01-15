import sys
input = sys.stdin.readline
t = list(input().strip())
if t[len(t)-1] != '0':
    print(-1)
else:
    t = int(''.join(t))
    temp = [300,60,10]
    abc=[0,0,0]
    for i in temp:
        abc[temp.index(i)] = t//i
        if t//i != 0:
            t = t%i
    for j in abc:
        print(j,end=" ")