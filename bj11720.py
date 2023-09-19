N  = int(input())
sum = 0
str1 = input()
int1 = list(map(int,str1))
for i in range(0,N,1):
    sum+=int1[i]
print(sum)