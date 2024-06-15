import sys
input = sys.stdin.readline


def main():
    n,k = map(int,input().split())
    count = 0
    while bin(n).count('1') > k:
        n += 1
        count += 1
    print(count)

if __name__ == "__main__":
    main()
    