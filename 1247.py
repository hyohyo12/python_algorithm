import sys
nums=[]
for i in range(3):
    for j in range(int(sys.stdin.readline())):
        nums.append(int(sys.stdin.readline()))
    if sum(nums)<0:
        print('-')
    elif sum(nums) == 0:
        print(0)
    else:
        print('+')
    nums.clear()