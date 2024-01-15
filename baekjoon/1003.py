fibo = [0,1]
for i in range(2,41):
    fibo.append(fibo[i-1]+fibo[i-2])
for i in range(int(input())):
    n = int(input())
    if n == 0:
        print("{0} {1}".format(1,0))
    else:
        print("{0} {1}".format(fibo[n-1],fibo[n]))