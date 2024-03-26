import sys
input = sys.stdin.readline

def divide_conquer(x,y,n):
    global num
    if x > r or x+n <= r or y > c or y+n <= c:
        num += (n**2)
        return
    if n > 2:
        n //= 2
        divide_conquer(x,y,n)
        divide_conquer(x,y+n,n)
        divide_conquer(x+n,y,n)
        divide_conquer(x+n,y+n,n)
    else:
        if x == r and y == c:
            print(num)
        elif x == r and y+1 == c:
            print(num+1)
        elif x+1 == r and y == c:
            print(num+2)
        else:
            print(num+3)
        sys.exit()
        


if __name__ == "__main__":
    n,r,c = map(int,input().split())
    num = 0
    divide_conquer(0,0,2**n)