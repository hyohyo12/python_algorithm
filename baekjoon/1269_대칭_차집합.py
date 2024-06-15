import sys
input = sys.stdin.readline


def main():
    a_len,b_len = map(int,input().split())
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    
    print(len(a-b)+len(b-a))

if __name__ == "__main__":
    main()