def find_in_string(string:str,ring:str):
    tmp = ring+ring[:len(string)]
    if string in tmp:
        return True
    else:
        return False

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    find_string = input().strip()
    n = int(input())
    count = 0
    for i in range(n):
        ring = input().strip()
        if find_in_string(find_string,ring):
            count+=1
    print(count)