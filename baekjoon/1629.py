import sys
input = sys.stdin.readline

def divide_conquer(a,b):
    if b == 0:
        return 1
    else:
        half = divide_conquer(a,b//2)
        if b%2 == 0:
            return (half * half) % c
        else:
            return (a * half*half)%c


if __name__ == "__main__":
    a,b,c = map(int,input().split())
    print(divide_conquer(a,b) % c)