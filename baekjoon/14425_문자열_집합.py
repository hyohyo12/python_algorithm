import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    res = 0
    n,m = map(int,input().split())
    words = defaultdict(int)
    for _ in range(n):
        words[input().strip()] = 1
    for _ in range(m):
        if (words[input().strip()] == 1):
            res += 1
    print(res)
    
    
if __name__ == "__main__":
    main()