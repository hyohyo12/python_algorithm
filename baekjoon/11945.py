import sys
input = sys.stdin.readline
n,m = map(int,input().split())
for i in range(n):
    temp = input().strip()
    temp = ''.join(list(reversed(temp)))
    print(temp)
    