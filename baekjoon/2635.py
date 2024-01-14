def find_sequence(num:int)->None:
    ans = []
    for i in range(1,num+1):
        tmp = [num,i]
        second = i
        first = num
        while True:
            next_num = first-second
            if next_num >=0:
                tmp.append(next_num)
                first = second
                second = next_num
            else:
                if len(tmp) > len(ans):
                    ans = tmp
                break
    print(len(ans))
    print(*ans)
if __name__ == "__main__":
    find_sequence(int(input()))