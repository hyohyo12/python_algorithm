divisor=[]
while True:
    n = int(input())
    if(n==-1):
        break
    else:
         for i in range(1,n):
            if n%i==0:
                 divisor.append(i)
    if(sum(divisor)==n):
        print("{0} =".format(n),end=" ")
        for i in range(0,len(divisor)):
            if(i==len(divisor)-1):
                print(divisor[i])
            else:
                print("{0} +".format(divisor[i]),end=" ")
        divisor.clear()
    else:
        print("{0} is NOT perfect.".format(n))
        divisor.clear()