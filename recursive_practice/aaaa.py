def max_representative_value(N, stars):
    # dp 배열 초기화
    dp = [0] * (N + 1)

    for i in range(2, N + 1):
        # 현재 날짜와 전날 별 중 거리가 가장 먼 별의 대푯값
        max_distance = max(abs(stars[i - 1][0] - stars[i - 2][0]) + abs(stars[i - 1][1] - stars[i - 2][1]), 0)
        
        # dp 갱신
        dp[i] = max(dp[i - 1], dp[i - 2] + max_distance)

    # 결과 반환
    return dp[N]

# 입력 처리
N = int(input())
stars = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_representative_value(N, stars))
