# N = int(input())
# if(N==0):
#     print(0)
# elif(N==1):
#     print(1)
# else:
#     N = list(map(int,str(N)))
#     N = list(reversed(N))
#     ten = 0
#     c=0
#     a=[]
#     j=0
#     for i in N:
#         ten+=i*(8**j)
#         j+=1
#     while ten!=1:
#         a.append(ten%2)
#         c=ten
#         ten=ten//2
#     a.append(c%2)

#     a= list(reversed(a))
#     for i in a:
#         print(i,end="")

print(bin(int(input(), 8))[2:])