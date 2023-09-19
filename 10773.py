import sys
input = sys.stdin.readline
stack = []
for i in range(int(input())):
    tmp = int(input())
    if tmp == 0:
        try:
            stack.pop()
        except:
            continue
    else:
        stack.append(tmp)
print(sum(stack))