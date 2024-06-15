import sys
input = sys.stdin.readline

def main():
    n = int(input())
    address = [list(map(int,input().split("."))) for _ in range(n)]
    

if __name__ == "__main__":
    main()