def find_num(n:int)->int:
    dp = [1 for _ in range(10)]
    for _ in range(n-1):
        for j in range(1,10):
            dp[j] += dp[j-1]
    return sum(dp) %10007
    

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    
    print(find_num(n))