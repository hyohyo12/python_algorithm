import heapq

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    seq = []
    for i in range(int(input())):
        heapq.heappush(seq,int(input()))
        if len(seq) % 2 == 0:
            print(min(seq[len(seq)//2],seq[(len(seq)//2)-1]))
        else:
            print(seq[len(seq)//2])
    