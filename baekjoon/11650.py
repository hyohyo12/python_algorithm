#11650 / 좌표 정렬하기
coordinate = []
for i in range(int(input())):
    coordinate.append(list(map(int,input().split())))
coordinate.sort()
coordinate.sort(key=lambda x : x[1])
for i in coordinate:
    print("{0} {1}".format(i[0],i[1]))
