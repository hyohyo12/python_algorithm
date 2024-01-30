import sys
import math
input = sys.stdin.readline

def optimal_coord(seq:list[tuple[int]],n:int,mid:int)->int:
    count = 0
    for x,a in seq:
        count += a
        if count >= mid:
            return x



if __name__ == "__main__":
    coord = []
    population = 0
    
    n = int(input())


    for _ in range(n):
        x,a = map(int,input().split())
        population += a
        coord.append((x,a))
    coord.sort(key=lambda x:x[0])
    mid = math.ceil((population)/2)
    print(optimal_coord(coord,n,mid))