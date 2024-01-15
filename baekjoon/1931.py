import sys
input = sys.stdin.readline
n = int(input())
ans = 1
meeting = []
for i in range(n):
    meeting.append(list(map(int,input().split())))
meeting.sort(key = lambda x:x[0])
meeting.sort(key=lambda x:x[1])

temp = meeting[0]
for i in range(1,n):
    if meeting[i][0] >= temp[1]:
        ans+=1
        temp = meeting[i]
print(ans)