n = 1000 - int(input())
ans = 0
# while n != 0:
#     if n//500 != 0:
#         ans+=n//500
#         n = n%500
#     elif n//100 != 0:
#         ans += n//100
#         n = n%100
#     elif n//50 != 0:
#         ans += n//50
#         n = n%50

ans += n//500
n = n%500
ans += n//100
n = n%100
ans += n//50
n = n%50
ans += n//10
n = n%10
ans += n//5
n = n%5
ans+=n//1
print(ans)