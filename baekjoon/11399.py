import sys
input = sys.stdin.readline
result = 0
temp = 0
n = int(input())
time = list(map(int,input().split()))
time = sorted(time)
for i in range(n):
    temp+=time[i]
    result+=temp
print(result)