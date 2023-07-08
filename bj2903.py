n=int(input())
a=[4]
p=1
f=2
res=0
for i in range(16):
    f+=p
    res=f**2
    a.append(res)
    p=p*2
print(a[n])