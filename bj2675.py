tc = int(input())
tmp=0
for i in range(tc):
    r,s=map(str,input().split())
    intR = int(r)
    strS = list(s)
    tmpList=['0' for i in range(len(strS)*intR)]
    for j in strS:
        for i in range(intR):
            tmpList[tmp]=j
            tmp+=1
    for i in tmpList:
        print(i,end="")
    print()
    tmpList.clear()
    tmp=0