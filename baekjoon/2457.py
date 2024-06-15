from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    
    flowers = []
    for _ in range(n):
        start_month,start_date,end_month,end_date = map(int,input().split())
        flowers.append((start_month*100+start_date,end_month*100+end_date))
    flowers.sort()
    flowers = deque(flowers)
    end_date = 301
    count = 0
    while flowers:
        if end_date >= 1201 or end_date < flowers[0][0]:
            break
        tmp_end_date = -1
        for i in range(len(flowers)):
            if end_date >= flowers[0][0]:
                tmp_end_date = max(tmp_end_date,flowers[0][1])
                flowers.popleft()
            else:
                break
        end_date = tmp_end_date
        count += 1
    print(0 if end_date < 1201 else count)