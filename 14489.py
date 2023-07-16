import sys
A, B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())
C *= 2
balance = A+B
if balance<C:
    print(balance)
else:
    print(balance-C)