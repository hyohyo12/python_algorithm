import sys
input = sys.stdin.readline
cnt = 1
op = []
stack = []
for i in range(int(input())):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        cnt+=1
        op.append('+')
    if stack[-1] == num:
        op.append('-')
        stack.pop()
    else:
        print('NO')
        break
else:
    for i in op:
        print(i)