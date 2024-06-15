import sys
input = sys.stdin.readline
def price_min(seq:list[tuple[int]],n:int,m:int):
    flag = False
    cost = sys.maxsize
    weight,same = 0,0
    for i in range(n):
        w,c = seq[i]
        weight += w
        if i >= 1 and seq[i-1][1] == c:
            same += c
        else:
            same = 0
        if weight >= m:
            flag = True
            cost = min(cost,c+same)
    
    return cost if flag else -1



if __name__ == "__main__":
    n,m = map(int,input().split())
    seq = []
    
    for _ in range(n):
        seq.append(tuple(map(int,input().split())))
    
    seq.sort(key=lambda x:(x[1],-x[0]))
    
    print(price_min(seq,n,m))