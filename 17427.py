import sys
def g(N):
    result = 0
    for i in range(1,N+1):
        result+=i*(N//i)
    return result
if __name__ == "__main__":
    print(g(int(sys.stdin.readline())))