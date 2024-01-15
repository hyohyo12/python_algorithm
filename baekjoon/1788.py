fibo = [0,1,1]
n = int(input())
if n == 0:
    print(0)
    print(0)
else:
    for i in range(3,abs(n)+1):
        fibo.append((fibo[i-1]+fibo[i-2])%1000000000)
    if n%2 == 0 and n<0:
        print(-1)
        print(fibo[abs(n)])
    else:
        print(1)
        print(fibo[abs(n)])