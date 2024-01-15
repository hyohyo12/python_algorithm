import sys
input = sys.stdin.readline
n = int(input())
string = list(input().strip())
ans = 0
for i in range(n):
    num = ord(string[i]) - 96
    ans+=num*(31**i)
print(ans % 1234567891)
# print(ans)