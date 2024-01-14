import sys
input = sys.stdin.readline

for i in range(int(input())):
    grade = 0
    tmp = 0
    ox = input().strip()
    for j in ox:
        if j == 'O':
            tmp+=1
            grade+=tmp
        else:
            tmp = 0
    print(grade)