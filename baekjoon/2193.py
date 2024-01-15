def fibo(n):
    fib = [0]* (n+1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib[n-1])
    
if __name__ =="__main__":
    fibo(int(input()))