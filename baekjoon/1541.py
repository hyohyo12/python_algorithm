expr = input().split('-')
tmp = sum(map(int,expr[0].split('+')))
for i in range(1,len(expr)):
    tmp -= sum(map(int,expr[i].split('+')))
print(tmp)