from collections import deque
max = 100000
def bfs(n,k):
    dist = [0]*(max+1)
    parent = [0]*(max+1)
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            temp = deque([x])
            while x != n:
                temp.appendleft(parent[x])
                x = parent[x]
            for i in temp:
                print(i,end=" ")
            break
        for i in (x+1,x-1,x*2):
            if 0 <= i <= max and dist[i] == 0:
                dist[i] = dist[x] + 1
                q.append(i)
                parent[i] = x
if __name__ == "__main__":
    n,k = map(int,input().split())
    bfs(n,k)