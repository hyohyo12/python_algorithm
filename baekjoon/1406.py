#1406 / 에디터
import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if str1:
            st2.append(str1.pop())
    elif command[0] == "D":
        if st2:
            str1.append(st2.pop())
    elif command[0] == "B":
        if str1:
            str1.pop()
    else:
        str1.append(command[1])
str1.extend(reversed(st2))
print(''.join(str1))