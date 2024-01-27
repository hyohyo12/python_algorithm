import heapq
def min_count(seq:list[int],n:int)->int:
    if n == 1:
        return 0
    count = 0
    while len(seq) != 1:
        num1,num2 = heapq.heappop(seq),heapq.heappop(seq)
        heapq.heappush(seq,num1+num2)
        count += num1+num2
    return count

if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    
    seq = []
    n = int(read())
    for i in range(n):
        heapq.heappush(seq,int(read()))
    print(min_count(seq,n))
    