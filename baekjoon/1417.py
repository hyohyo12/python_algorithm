import sys
input = sys.stdin.readline
candidate =[]
n = int(input())
dasom = int(input())
counter = 0
if n == 1:
    print(0)
else: 
    for _ in range(n-1):
        candidate.append(int(input()))
    while dasom <= max(candidate):
        candidate[candidate.index(max(candidate))] -= 1
        dasom +=1
        counter += 1
    print(counter)