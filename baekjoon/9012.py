import sys
input = sys.stdin.readline
for i in range(int(input())):
    stack = []
    tmp = input().strip()
    for i in tmp:
        if i == ')':
            try:
                stack.pop()
            except:
                print('NO')
                break
        else:
            stack.append(i)
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')