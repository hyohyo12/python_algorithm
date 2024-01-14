def fibo2(n):
    global count2
    fibo = [1,1]
    for i in range(2,n):
        fibo.append(fibo[i-1] + fibo[i-2])
        count2 += 1
    return fibo[n-1]

if __name__ =="__main__":
    count = 0
    count2 = 0
    n = int(input())
    print(fibo2(n),count2)