def all_part_sum(seq:list[int],n: int)-> None:
    for i in range(1,n+1):
        for j in range(1,n+1):
            seq[i][j] +=(seq[i-1][j] + seq[i][j-1] - seq[i-1][j-1])

def find_part_sum(x1:int,y1:int,x2:int,y2:int,seq:list[list[int]])->int:
    return seq[x2][y2] - seq[x2][y1-1] - seq[x1-1][y2] +seq[x1-1][y1-1]





if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n,m = map(int,input().split())
    seq = [[0 for _ in range(n+1)]]
    for i in range(n):
        seq.append([0] + list(map(int,input().split())))
    all_part_sum(seq,n)
    for j in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        print(find_part_sum(x1,y1,x2,y2,seq))