import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int,input().split()))
ans = [1]
for i in range(n-1,-1,-1):   
        if i+line[i-1] < n:
            ans.append(ans[n-i-1])