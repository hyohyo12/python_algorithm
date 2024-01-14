#11050 / 이항 계수1
import sys
input = sys.stdin.readline
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
if __name__ == "__main__":
    n,k = map(int,input().split())
    print(factorial(n) // (factorial(n-k) * factorial(k)))