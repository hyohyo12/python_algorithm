chess=[]
count=0
for i in range(8):
    a=list(input())
    chess.append(a)
for i in range(8):
    if i%2!=0:
        for j in range(1,8,2):
            if chess[i][j]=='F':
                count+=1
    elif i%2 == 0:
        for j in range(0,8,2):
            if chess[i][j]=='F':
                count+=1
print(count)