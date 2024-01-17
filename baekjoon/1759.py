gather = ['a','e','i','o','u']
def all_case(l:int,c:int,seq:list[str],start,cur:list[str],visited:list[bool],a_cnt:int,b_cnt:int)->None:
    if len(cur) == l:
        if a_cnt >= 1 and b_cnt>=2:
            print(''.join(cur))
        return
    for i in range(start,c):
        if not visited[i]:
            if seq[i] in gather:
                a_cnt+=1
                visited[i] = True
                cur.append(seq[i])
                all_case(l,c,seq,i+1,cur,visited,a_cnt,b_cnt)
                visited[i] = False
                cur.pop()
                a_cnt-=1
            else:
                b_cnt += 1
                visited[i] = True
                cur.append(seq[i])
                all_case(l,c,seq,i+1,cur,visited,a_cnt,b_cnt)
                visited[i] = False
                cur.pop()
                b_cnt-=1
                
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    l,c = map(int,input().split())
    seq = list(input().strip().split())
    seq.sort()
    visited = [False]*(c)
    all_case(l,c,seq,0,[],visited,0,0)