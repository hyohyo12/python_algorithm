import sys
input = sys.stdin.readline

def min_count(seq: list[int])->int:
    count = 0
    count += seq[6]

    
    count += 1*seq[5]
    seq[1] = min(seq[1]-(11*seq[1]),0)
    
    while seq[4]:
        area = 20
        area -= min(seq[2],5)*4
        seq[4] -= 1
        seq[2] = max(seq[2]-5,0)
        seq[1] = max(0,seq[1]-area)
        count += 1
    
    while seq[3]:
        area = 36 - (9*min(4,seq[3]))
        if seq[3] >= 4:
            seq[3] -= 4
            area = 0
        elif seq[3] == 3:
            area -= min(seq[2],1)*4
            seq[2] = max(0,seq[2]-1)
        elif seq[3] == 2:
            area -= min(3,seq[2])*4
            seq[2] = max(0,seq[2]-3)
        else:
            area -= min(5,seq[2])*4
            seq[2] = max(0,seq[2]-5)
        seq[1] = max(seq[1]-area,0)
        count += 1
    while seq[2]:
        area = 36 - min(9,seq[2])*4
        seq[2] = max(0,seq[2]-9)
        seq[1] = max(0,seq[1]-area)

    while seq[1]:
        seq[1] = max(0,seq[1]-36)
        count += 1
    return count
    
if __name__ == "__main__":
    seq = [0] + [int(input()) for _ in range(6)]
    print(min_count(seq))