import math
import sys
input = sys.stdin.readline

x = 1000000007

def expected_value(n:int,s:int):
    return s * power(n,x-2) % x
def power(num,exp):
    if exp == 1:
        return num
    if exp % 2:
        return (num * power(num,exp-1)) % x
    else:
        half = power(num,exp//2)
        return half * half % x


def main():
    m = int(input())
    sum = 0
    for _ in range(m):
        n,s = map(int,input().split())
        gcd = math.gcd(n,s)
        n //= gcd
        s //= gcd
        sum += expected_value(n,s)
        sum %= x
    print(sum)
if __name__ == "__main__":
    main()