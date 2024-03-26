from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))
count = Counter(seq)
max_count = max(count.values())
if len(seq)%2 == 0:
    if max_count > len(seq)//2:
        print('NO')
    else:print('YES')
else:
    if max_count > len(seq)//2+1:
        print('NO')
    else:print('YES')
