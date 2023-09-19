n = int(input())
for i in range(0,n):
    if i+sum(list(map(int,str(i)))) == n:
        print(i)
        break
else:
    print(0)