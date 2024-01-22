from collections import deque
def fastival(seq,n,start,end):
    q = deque([start])
    visited = [False for _ in range(n+1)]
    while q:
        x,y = q.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return "happy"
        for i in range(n):
            if not visited[i]:
                if abs(x-seq[i][0]) + abs(y-seq[i][1]) <= 1000:
                    q.append((seq[i][0],seq[i][1]))
                    visited[i] = True
    return "sad"



if __name__ == "__main__":
    import sys
    input =sys.stdin.readline
    
    for i in range(int(input())):
        seq = []
        n = int(input())
        start = list(map(int,input().split()))
        for i in range(n):
            seq.append(tuple(map(int,input().split())))
        end = tuple(map(int,input().split()))
        print(fastival(seq,n,start,end))
    