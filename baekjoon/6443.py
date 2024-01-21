def all_anagram(s:str,cur:list[str],visited)->None:
    if len(cur) == len(s):
        print(cur)
        return
    for i in visited:
        if visited[i]:
            visited[i] -= 1
            cur+=i
            all_anagram(s,cur,visited)
            visited[i] += 1
            cur = cur[:-1]


if __name__ == "__main__":
    import sys
    from collections import defaultdict
    read = sys.stdin.readline
    n = int(read())
    for i in range(n):
        visited = defaultdict(int)
        s = sorted(list(read().strip()))
        for i in s:
            visited[i] += 1
        all_anagram(s,'',visited)
