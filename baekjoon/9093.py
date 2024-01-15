import sys
input = sys.stdin.readline
for i in range(int(input())):
    words = list(input().strip().split(" "))
    for j in range(0,len(words)):
        words[j] = ''.join(list(reversed(words[j])))
    print(' '.join(words))