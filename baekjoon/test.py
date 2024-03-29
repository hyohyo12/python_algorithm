# import sys
# import heapq
# input = sys.stdin.readline


# if __name__ == "__main__":
#     n,k = map(int,input().split())
    
#     dia_seq = [] 
#     for _ in range(n):
#         m,v = map(int,input().split())
#         heapq.heappush(dia_seq,(-v,m))
    
#     bag_seq = [int(input()) for _ in range(k)]

#     bag_seq.sort(reverse=True)
    
#     bag = [[] for _ in range(len(bag_seq))]
#     ans = 0
#     for idx,w in enumerate(bag_seq):
#         for _ in range(len(dia_seq)):
#             v,m = heapq.heappop(dia_seq)
#             v = abs(v)
#             if len(bag[idx]) > 0 and m <= w:
#                 prev_v,prev_m = bag[idx].pop()
#                 if prev_v < v:
#                     ans -= prev_v
#                     bag[idx].append((v,m))
#                     ans += v
#                     heapq.heappush(dia_seq,(-prev_v,prev_m))
#                 elif prev_v == v:
#                     if prev_m < m:
#                         bag[idx].append((prev_v,prev_m))
#                         heapq.heappush(dia_seq,(-v,m))
#                     else:
#                         bag[idx].append((v,m))
#                         ans -= prev_v
#                         ans += v
#                         heapq.heappush(dia_seq,(-prev_v,prev_m))
#                 else:
#                     bag[idx].append((prev_v,prev_m))
#                     heapq.heappush(dia_seq,(-v,m))
#             elif len(bag[idx]) == 0 and m <= w:
#                 ans += v
#                 bag[idx].append((v,m))
#     print(ans)




# import sys
# input = sys.stdin.readline


# if __name__ == "__main__":
#     ans = 0
#     #A-J 까지 (자릿수,맨 왼쪽에 오는지) 를 저장하는 리스트
#     alpha = [[0,False] for _ in range(10)]
#     n = int(input())

#     for i in range(n):
#         s = input().strip()  # 문자열 입력
#         alpha[ord(s[0])-65][1] = True #첫번째 요소로 오면 맨 왼쪽에 온다는 뜻이므로 True로 변환
#         m = 1 #자릿 수를 저장할 m
#         for c in range(len(s)-1,-1,-1): # 뒷자리(자릿수 검사를 위해) 부터 검사
#             alpha[ord(s[c])-65][0] += m #자릿수를 저장
#             m*=10 #자릿 수를 더하기 위해 10을 곱한다.
            
#     alpha.sort(reverse=True) #탐색을 위해 오름차순 정렬
    
#     if alpha[9][1]: #끝값을 확인하는 이유 만약 True 면 확인해야함 위에 False 있는지 함부로 삭제 못하므로
#         for i in range(8,-1,-1): # 끝값이라도 어느 숫자의 처음이 있다는 말로 숫자를 할당해므로 위에서부터 False 검사
#             if not alpha[i][1]: # 만약 False면 0을 할당할 것이므로 해당 값 지운다
#                 del alpha[i] #오름차순으로 정렬하고 탐색은 뒤에서부터 진행하므로 처음 False 나온 값이 제일 작은 값이므로
#                 break#바로 지우고 Break
#     for i in range(9):#0~8까지 순회(0,1,2,3,4,5,6,7,8)
#         ans += alpha[i][0] * (9-i) #(9,8,7,6,5,4,3,2,1)->  0은 이미 del함수로 지웠으므로
#     print(ans)



a = 0
while a < 10:
    a += 1
print(a)