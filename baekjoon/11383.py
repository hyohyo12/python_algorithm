import sys
input = sys.stdin.readline
n,m = map(int,input().split())
words = []
Eyfa = True
for i in range(n):
    words.append(list(input().strip()))
words2 = []
for j in range(n):
    words2.append(input().strip())
for k in range(0,n):
    for i in range(0,m):
        words[k][i] = words[k][i] + words[k][i]
    if ''.join(words[k]) == words2[k]:
        continue
    else:
        Eyfa = False
        break
if Eyfa:
    print("Eyfa")
else:
    print("Not Eyfa")