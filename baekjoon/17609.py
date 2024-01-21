def pailndrome(seq:str)->int:
    left = 0
    right = len(seq)-1
    while left < right:
        if seq[left] == seq[right]:
            left += 1
            right -= 1
            continue
        else:
            if seq[left] == seq[right-1]:
                tmp = seq[left:right]
                if tmp[::-1] == tmp:
                    return 1
            if seq[left+1] == seq[right]:
                tmp = seq[left+1:right+1]
                if tmp == tmp[::-1]:
                    return 1
            break
    else:
        return 0
    return 2
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    for _ in range(int(input())):
        word = input().strip()
        print(pailndrome(word))