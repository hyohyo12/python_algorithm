import sys
input = sys.stdin.readline
n = int(input())
attendance = {}
for i in range(n):
    a,b = input().split()
    if b == 'enter':
        attendance[a] = b
    else:
        del attendance[a]
attendance = sorted(attendance.keys(),reverse=True)
for i in attendance:
    print(i)