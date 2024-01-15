n = input()
n = list(map(int,str(n)))
count = 0
for i in range(0,len(n)-1):
    if n[i] != n[i+1]:
        count+=1
print((count+1)//2)