from collections import deque
import sys
input = sys.stdin.readline


def bfs(n:int,k:int):
    visited = [0 for _ in range(100001)]
    count = 0
    start = n
    result = 0
    q = deque([start])
    while q:
        x = q.popleft()
        tmp = visited[x]
        if x == k:
            result = tmp
            count += 1
            continue
        for i in [x-1,x+1,x*2]:
            if 0 <= i < 100001 and (visited[i] == 0 or visited[i] == visited[x]+1):
                q.append(i)
                visited[i] = visited[x] + 1
    return result,count
def main():
    n,k = map(int,input().split())
    for i in bfs(n,k):
        print(i)



if __name__ == "__main__":
    main()