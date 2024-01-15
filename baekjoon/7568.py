import sys
input = sys.stdin.readline
count = 1
rank = []
n = int(input())
people = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                count+=1
            else:
                continue
    rank.append(count)
    count = 1

for k in rank:
    print(k,end=" ")
