import sys
input = sys.stdin.readline



def main():
    n,m = map(int,input().split())
    know_set = set(input().split()[1:])
    board = []
    for _ in range(m):
        board.append(set(input().split()[1:]))
    
    for _ in range(m):
        for party in board:
            if party & know_set:
                know_set = know_set.union(party)
    
    count = 0
    for party in board:
        if party & know_set:
            continue
        count += 1
    print(count)
    
    
if __name__ == "__main__":
    main()