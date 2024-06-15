import sys
from itertools import permutations
input = sys.stdin.readline

#최고 점수를 구하는 함수
def find_max_score(seq:list[list[int]],n:int):
    res = 0
    
    res = -(sys.maxsize)
    
    for prob in permutations(range(1,9),8):
        prob = list(prob)
        now = prob[0:3] + [0] + prob[3:]
        runner,score = 0,0
        for i in range(n):
            first,second,third = 0,0,0
            out = 0
            while out < 3:
                if seq[i][now[runner]] == 0:
                    out += 1
                    runner = (1+runner) % 9
                    continue
                
                elif seq[i][now[runner]] == 1:
                    score += third
                    first,second,third = 1,first,second
                    
                elif seq[i][now[runner]] == 2:
                    score += (second+third)
                    first,second,third = 0,1,first
                    
                elif seq[i][now[runner]] == 3:
                    score += (first+second+third)
                    first,second,third = 0,0,1
                    
                elif seq[i][now[runner]]== 4:
                    score += (first+second+third+1)
                    first,second,third = 0,0,0
                    
                runner = (1+runner) % 9
        res = max(res,score)
    return res

def main():
    #입력
    #N -> 이닝수
    N = int(input())
    seq = [list(map(int,input().split())) for _ in range(N)]
    print(find_max_score(seq,N))

if __name__ == "__main__":
    main()