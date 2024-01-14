def get_under_prime(n):
    prime_list = [True] * (n+1)
    prime_list[0] = prime_list[1] = False
    for i in range(2,int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i*i,n+1,i):
                prime_list[j] = False
    return prime_list

def get_k_number(n,k):
    prime_list = get_under_prime(n)
    res = [1]*(n+1)
    for i in range(1,n+1):
        if prime_list[i] and i > k:
            for j in range(i,n+1,i):
                res[j] = 0
    return sum(res)-1


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    k = int(input())
    print(get_k_number(n,k))