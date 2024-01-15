import sys
input = sys.stdin.readline
n = int(input())
trees = list(map(int,input().split()))
trees.sort(reverse=True)
for i in range(n):
    trees[i] = trees[i]+i+1
print(max(trees)+1)        
        