def get_num(n,k):
    minimum = k*(k+1)//2
    if  minimum > n:
        return -1
    if (n-minimum) % k == 0:
        return k-1
    else:
        return k
    
if __name__ == "__main__":
    n,k = map(int,input().split())
    print(get_num(n,k))