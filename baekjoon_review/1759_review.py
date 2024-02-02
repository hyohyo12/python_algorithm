consonant = ['a','e','i','o','u']

def passwd(seq:list[str],l:int,c:int,cur:list[str],c_count:int,v_count:int,visited:list[bool],start:int):
    if len(cur) == l:
        if c_count >= 1 and v_count >= 2:
            print(''.join(cur))
            return
    
    for i in range(start,c):
        if not visited[i]:
            visited[i] = True
            cur.append(seq[i])
            if seq[i] in consonant:
                c_count += 1
                passwd(seq,l,c,cur,c_count,v_count,visited,i+1)
                c_count -= 1
            else:
                v_count += 1
                passwd(seq,l,c,cur,c_count,v_count,visited,i+1)
                v_count -= 1
            cur.pop()
            visited[i] = False



if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    
    l,c = map(int,read().split())
    seq = list(read().strip().split())
    
    seq.sort()
    visited = [False for _ in range(c)]
    
    passwd(seq,l,c,[],0,0,visited,0)