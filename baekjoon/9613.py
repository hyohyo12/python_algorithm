import sys
input = sys.stdin.readline
def gcd(a,b):
    if  a>b:
        a,b = b,a
    while(b):
        a,b = b,a%b
    return a
if __name__ == "__main__":
    for i in range(int(input())):
        result = 0
        n = list(map(int,input().split()))
        for j in range(1,len(n)):
            for k in range(j+1,len(n)):
                result+=gcd(n[j],n[k])
        print(result)
        