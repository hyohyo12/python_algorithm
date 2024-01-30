import math
def minimum(seq:list[int]):
    count = 1
    s_left,h_left = 6,0
    for i in range(1,7):
        h = math.ceil(((seq[i]*i)/6))
        #밑에 변이 부족한 경우
        if s_left - ((seq[i]*i))%6 < 0:
            #한 칸 올라가고 높이가 부족한 경우
            if h_left+h+1> 6: # 최대한 붙이고 새로운 판
                count += 1
                s_left,h_left = 6,0
            #한 칸 올라가고 높이가 충분한 경우
            else:
                s_left = 6 - ((seq[i]*i))%6 #남은 변의 길이
                h_left -= (1+h) #남은 높이 길이
        #높이가 부족한 경우
        #최대한 붙이도 다음 판
        


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    seq = [0]
    for i in range(6):
        seq.append(int(input()))