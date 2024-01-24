def minimum(seq:list[int])->int:
    count = 0
    
    if seq[6]:
        count += seq[6]
    
    while seq[5]:
        area = 36 - 5*5
        seq[5] -= 1
        seq[1] = max(seq[1]-area,0)
        count += 1
    
    while seq[4]:
        area = 36 - 4*4
        area -= min(seq[2],5)*4
        seq[4] -= 1
        seq[2] = max(seq[2]-5,0)
        seq[1] = max(seq[1]-area,0)
        count += 1
        
    while seq[3]:
        area = 36 - min(seq[3],4)*9
        if seq[3] >= 4:
            seq[3] -= 4
            count+=1
            area = 0
        elif seq[3] == 3:
            seq[3] -= 3
            area -= min(seq[2],1)*4
            seq[2] = max(seq[2]-1,0)
        elif seq[3] == 2:
            area = min(seq[2],3)*4
            seq[3] -= 2
            seq[2] = max(seq[2]-3,0)
        else:
            area -= min(5,seq[2])*2
            seq[3] -= 1
            seq[2] = max(seq[2]-5,0)
        seq[1] = max(seq[1]-area,0)
        count += 1
    
    while seq[2]:
        area = 36 - min(9,seq[i])*4
        seq[2] = max(seq[2]-9,0)
        seq[1] = max(seq[1]-area,0)
        count += 1
        
    while seq[1]:
        seq[1] = max(0,seq[1]-36)
        count += 1
        
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    seq = [0]
    for i in range(6):
        seq.append(int(input()))
    print(minimum(seq))