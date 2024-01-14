def fib(n):
    fibo = [0,1]
    for i in range(2,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return((fibo[n-1],fibo[n]))
if __name__ =="__main__":
    a,b = fib(int(input()))
    print(a,b)