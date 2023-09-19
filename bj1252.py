a,b = map(int,input().split())
a=list(map(int,(str(a))))
b=list(map(int,(str(b))))
a = list(reversed(a))
b = list(reversed(b))
count=0
if(len(a)>=len(b)):
    for i in range(0,len(a)):
        if(count==0):
            try:
                a[i] = a[i]+b[i]
            except:
                a[i]=a[i]
            if(a[i]==2):
                a[i]=0
                if(len(a)-1==i):
                    a.append(1)
                else:
                    count=1
            else:
                count=0
        else:
            try:
                a[i] = a[i]+b[i]+1
            except:
                a[i]=a[i]+1
            if(a[i]==3):
                a[i]=1
                if(i==len(a)-1):
                    a.append(1)
                else:
                    count=1
            elif(a[i]==2):
                a[i]=0
                if(i==len(a)-1):
                    a.append(1)
                else:
                    count=1
            else:
                count=0
    a=list(reversed(a))
    for i in(a):
        print(i,end="")
if(len(a)<len(b)):
    for i in range(0,len(b)):
        if(count==0):
            try:
                b[i] = a[i]+b[i]
            except:
                b[i]=b[i]
            if(b[i]==2):
                b[i]=0
                if(len(b)-1==i):
                    b.append(1)
                else:
                    count=1
            else:
                count=0
        else:
            try:
                b[i] = a[i]+b[i]+1
            except:
                b[i]=b[i]+1
            if(b[i]==3):
                b[i]=1
                if(i==len(b)-1):
                    b.append(1)
                else:
                    count=1
            elif(b[i]==2):
                b[i]=0
                if(i==len(b)-1):
                    b.append(1)
                else:
                    count=1
            else:
                count=0
    b=list(reversed(b))
    for i in(b):
        print(i,end="")