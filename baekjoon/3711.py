for i in range(int(input())):
    result = 0
    g = int(input())
    student = [int(input()) for i in range(g)]
    if g == 1:
        print(1)
    else:
        while True:
            result+=1
            if len({i % result for i in student}) == g:
                print(result)
                break