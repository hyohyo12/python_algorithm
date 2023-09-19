import sys
input = sys.stdin.readline
numbers = []
temp = []
for i in range(10):
    numbers.append(int(input()))

for i in range(0,10):
    add= numbers[i]
    for j in range(i+1,10):
        add = add + numbers[j]
        if add > 100:
            break
        else:
            temp.append(add)
