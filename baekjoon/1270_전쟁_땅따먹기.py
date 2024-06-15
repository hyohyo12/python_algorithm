import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        seq = defaultdict(int)
        data = list(map(int,input().split()))
        threshold = data[0] // 2
        for d in data[1:]:
            seq[d] += 1
            if seq[d] > threshold:
                print(d)
                break
        else:
            print("SYJKGW")

if __name__ == "__main__":
    main()