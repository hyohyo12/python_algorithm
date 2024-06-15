import sys
import heapq
input = sys.stdin.readline


def main():
    #접두어를 사전순으로 저장할 힙큐
    q = []
    s = input().strip()
    
    for i in range(len(s)):
        heapq.heappush(q,''.join(s[i:]))
    
    for _ in range(len(s)):
        print(heapq.heappop(q))


if __name__ == "__main__":
    main()