import sys
from collections import deque
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    counter = 0
    n,m = map(int,input().split())
    queue = deque(map(int,input().split()))
    while queue:
        big = max(queue)
        front = queue.popleft()
        m -= 1
        if big == front:
            counter += 1
            if m < 0:
                print(counter)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1