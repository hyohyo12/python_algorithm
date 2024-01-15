#16953 / A -> B
from collections import deque

# def ans(a,b):
#     cnt = 1
#     while b!=a:
#         temp = b
#         if b%2 == 0:
#             cnt += 1
#             b = b//2
#         elif b%10 == 1:
#             b = b//10
#             cnt += 1
#         if temp == b:
#             return -1
#     return cnt

# if __name__ == "__main__":
#     a,b = map(int,input().split())
#     print(ans(a,b))

#BFS 버전

def bfs(a,b):
    q = deque()
    q.append((a,1))
    while q:
        n,count = q.popleft()
        if n > b:
            continue
        if n == b:
            return count
        else:
            q.append((n*2,count+1))
            q.append((int(str(n)+"1"),count+1))
    return -1
if __name__ == "__main__":
    a,b = map(int,input().split())
    print(bfs(a,b))