
# if __name__ == "__main__":
#     visited = [False for _ in range(9)]
#     all_probablity = []
#     arr = [0,1,2,4,5,6,7,8]
#     def my_permutation(cur:list[int]):
#         global all_probablity
#         if len(cur) == 8:
#             tmp = cur[:]
#             all_probablity.append(tmp)
#             return
#         for i in range(8):
#             if not visited[i]:
#                 visited[i] = True
#                 cur.append(arr[i])
#                 my_permutation(cur)
#                 cur.pop()
#                 visited[i] = False
#     my_permutation([])
#     for p in all_probablity:
#         print(*p)
# from collections import deque,defaultdict

# # 입력 받은 숫자들을 리스트로 저장
# graph = deque(map(int, input().split()))

# # 빈 딕셔너리 생성
# fruits = defaultdict(int)

# # graph 안에 있는 숫자들을 반복하면서 카운팅
# for num in graph:
#     # 딕셔너리에 이미 해당 숫자가 있는지 확인 후, 있으면 카운트 증가
#     if fruits[num]:
#         fruits[num] += 1
#     else:
#         fruits[num] = 1  # 없으면 해당 숫자를 키로 추가하고 카운트를 1로 초기화

# print(fruits)


def update_matrix(matrix):
    # 예를 들어, 첫 번째 요소를 0으로 변경
    matrix[0][0] = 0
    # 모든 요소에 1을 더하기
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

def main():
    # 2차원 배열 (리스트)
    my_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # 함수에 배열을 인자로 전달
    update_matrix(my_matrix)
    
    # 변경된 배열 출력
    print(my_matrix)
    # 출력: [[1, 3, 4], [5, 6, 7], [8, 9, 10]]

if __name__ == "__main__":
    main()