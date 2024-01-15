#15886 / 내 선물을 받아줘 2 
def ans(line,n):
    cnt = 0
    for i in range(n):
        if line[i] == 'E' and line[i-1] == 'W':
            cnt += 1
    return cnt
    
if __name__ == "__main__":
    n = int(input())
    line = input()
    print(ans(line,n))