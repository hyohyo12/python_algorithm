import sys
input = sys.stdin.readline
decoding = {"AA": "A","AG":"C","AC":"A","AT":"G","GA":"C","GG":"G","GC":"T","GT":"A","CA":"A","CG":"T","CC":"C","CT":"G","TA":"G","TG":"A","TC":"G","TT":"T"}
n = int(input())
base = list(input().strip())
counter = n
while counter != 1:
    temp = decoding[base.pop()+base.pop()]
    base.append(temp)
    counter -= 1
print(base[0])