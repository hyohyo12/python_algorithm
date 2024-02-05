# import sys
# input = sys.stdin.readline

# a = int(input())
# b = int(input())
# c = int(input())

# print(a+b-c)
# a = int(str(a)+str(b))-c
# print(a)






n = int(input())
seq = [0] + list(map(int,input().split()))
ans = 0
start,end = 1,1
while True:
    if end == n:
        if tmp <= seq[end]:
            ans += 1
        break
    elif start == end:
        tmp = seq[end]
        s_tmp = seq[start]
        end += 1
    elif seq[end] > tmp:
        tmp = seq[end]
        end += 1
        ans += 1
    elif seq[end] < tmp and start < end:
        if s_tmp >= seq[start]:
            ans += 1
        s_tmp = seq[start]
        start += 1
print(ans+n)






# import sys
# from collections import deque
# input = sys.stdin.readline
# def bfs(graph_1,graph_2,visited,r,c,d):
#     q = deque([(r,c,d,0)])
#     ans = 0
#     visited[r][c] = True
#     while q:
#         y,x,degree,graph = q.popleft()
        
#         if graph == 0:
            




# if __name__ =="__main__":
#     h,w = map(int,input().split())
#     r,c,d = map(int,input().split())
    
#     graph_1 = [list(map(int,input().strip())) for _ in range(h)]
#     graph_2 = [list(map(int,input().strip())) for _ in range(h)]
    
#     visited = [[False for _ in range(w)] for _ in range(h)]
    
    
    
    


# import sys
# import heapq
# input = sys.stdin.readline

# n,k,m = map(int,input().split())
# soket = list(map(int,input().split()))
# d_seq = list(map(int,input().split()))
# d_seq.sort()

# left_soket = [k-1] + [i-1 for i in soket]
# zero_list = []
# while d_seq:
#     x = d_seq.pop()
#     idx = min(n,x)
#     if n < 0:
#         d_seq.append(x)
#         break
    
#     if left_soket[idx] > 0:
#         left_soket[idx] -= 1
#     elif left_soket[idx] <= 0:
#         d_seq.append(x)
#         n -= 1

# print(m-len(d_seq))