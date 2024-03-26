import sys
input = sys.stdin.readline

def min_carry(crane_seq:list[int],box_seq:list[int],m:int)->int:
    cnt = -1
    if crane_seq[0] < box_seq[0]:
        return cnt
    cnt = 0
    while len(box_seq) > 0:
        for crane in crane_seq:
            if box_seq and crane < box_seq[-1]:
                continue
            for box in box_seq:
                if box_seq and box <= crane:
                    box_seq.remove(box)
                    break
        cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    crane_seq = list(map(int,input().split()))
    crane_seq.sort(reverse=True)
    m = int(input())
    box_seq = list(map(int,input().split()))
    box_seq.sort(reverse=True)
    
    print(min_carry(crane_seq,box_seq,m))