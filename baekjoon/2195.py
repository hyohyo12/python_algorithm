def low_copy(s:str,p:str)->int:
    count = 0
    index = 0
    while index < len(p):
        c_index,cur,max_len = 0,0,0
        while c_index < len(s) and index+cur < len(p):
            if s[c_index] == p[index+cur]:
                cur += 1
                max_len = max(cur,max_len)
            else:
                cur = 0
            c_index += 1
        index += max_len
        count+=1
    return count



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    s = input().strip()
    p = input().strip()
    
    print(low_copy(s,p))