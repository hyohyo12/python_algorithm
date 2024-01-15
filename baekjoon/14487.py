import sys
input = sys.stdin.readline
n = int(input())
city = list(map(int,input().split()))
print(sum(city)-max(city))