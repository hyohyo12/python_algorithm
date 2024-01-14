import sys
input = sys.stdin.readline
primeNum = [True for i in range(1000000)]
primeNum[0] = False
primeNum[1] = False
for i in range(2,int(1000000**0.5)+1):
    if primeNum[i] == True:
        for j in range(i*2,1000000,i):
            if primeNum[j] == True:
                primeNum[j] = False

while True:
    n = int(input())
    if n == 0 : 
        break
    else:
        for i in range(3,n,2):
            if primeNum[i] == True:
                if primeNum[n-i] == True:
                    print("{0} = {1} + {2}".format(n,i,n-i))
                    break
                else:
                    continue
        else:
            print("Goldbach's conjecture is wrong.")