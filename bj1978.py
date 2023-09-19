n=int(input())
numbers = map(int,input().split())
numbers=list(numbers)
divisors=[]
count=0
for i in range(n):
    for j in range(1,numbers[i]):
         if(numbers[i]%j==0):
             divisors.append(j)
    if(len(divisors)==1):
        count+=1
    divisors.clear()
print(count)