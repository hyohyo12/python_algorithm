import sys
input = sys.stdin.readline
n = int(input())
pre = []
count = 0
for i in range(n):
    words = input().strip()
    for j in range(0,len(words)):
        if words[j] in pre:
            if words[j-1] == words[j]:
                continue
            else:
                break
        else:
            pre.append(words[j])
    else:
        count+=1
    pre.clear()
print(count)