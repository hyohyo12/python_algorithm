import sys
input = sys.stdin.readline
count = [0 for i in range(10001)]
for i in range(int(input())):
    num = int(input())
    count[num] += 1
for j in range(10001):
    if count[j] == 0:
        continue
    else:
        for k in range(count[j]):
            print(j)