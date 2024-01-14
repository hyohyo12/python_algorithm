def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    max_divisor = int(n**0.5)+1
    for i in range(3,max_divisor,2):
        if n%i == 0:
            return False
    return True



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    for i in range(int(input())):
        n = int(input())
        while True:
            if is_prime(n):
                break
            n+=1
        print(n)