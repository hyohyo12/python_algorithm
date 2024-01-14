import sys
input = sys.stdin.readline

cows = []
for i in range(int(input())):
    cows.append(list(map(int,input().split())))
cows.sort(key=lambda x:(x[0],x[1]))


time = -1
for i in range(len(cows)):
    if time < cows[i][0]:
        time = cows[i][0]+cows[i][1]
    else:
        time+=cows[i][1]
print(time)