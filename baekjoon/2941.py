import sys
input = sys.stdin.readline
words = input().strip()
croatia = ['c=','c-','dz=','z=','s=','nj','lj','d-']
for i in croatia:
    words = words.replace(i,'*')
print(len(words))