import sys
input = sys.stdin.readline

ALPH={'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2,
    'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 'N': 2, 'O': 1,
    'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1,
    'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

def get_per(nam:list[str],her:list[str])->str:
    dp = [[1]*i for i in range(len(nam)*2,1,-1)]
    for i in range(len(dp[0])-1,-1,-2):
        dp[0][i-1], dp[0][i] = ALPH[nam.pop()],ALPH[her.pop()]
    for i in range(1,len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = (dp[i-1][j]+dp[i-1][j+1])%10
    return str(dp[-1][0])+str(dp[-1][1])



if __name__ == "__main__":
    names = []
    for i in range(2):
        names.append(list(input().strip()))
    print(get_per(names[0],names[1]))