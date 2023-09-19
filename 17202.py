num1 = list(map(int,input()))
num2 = list(map(int,input()))
tmp = []
for i in range(0,8):
    tmp.append(num1[i])
    tmp.append(num2[i])
while len(tmp) != 2:
    new = []
    for i in range(0,len(tmp)-1):
        new.append((tmp[i]+tmp[i+1])%10)
    tmp = new.copy()
for i in tmp:
    print(i,end="")