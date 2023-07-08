a = [input() for i in range(5)]
for i in range(15):
    for j in range(5):
        if(len(a[j])>i):
            print(a[j][i],end="")