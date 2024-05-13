
if __name__ == "__main__":
    visited = [False for _ in range(9)]
    all_probablity = []
    arr = [0,1,2,4,5,6,7,8]
    def my_permutation(cur:list[int]):
        global all_probablity
        if len(cur) == 8:
            tmp = cur[:]
            all_probablity.append(tmp)
            return
        for i in range(8):
            if not visited[i]:
                visited[i] = True
                cur.append(arr[i])
                my_permutation(cur)
                cur.pop()
                visited[i] = False
    my_permutation([])
    for p in all_probablity:
        print(*p)
        