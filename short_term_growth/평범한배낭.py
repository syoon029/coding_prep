# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
# 입력으로 주어지는 모든 수는 정수이다.

#weight 테이블로, 그 안에 value들을 다룬다면 어렵지않다 , ex) w 무게가 6이고 value는 13

# w A  B  C   D
# 0 0  0  0   0
# 1 0  0  0   0
# 2 0  0  0   0
# 3 0  0  6   6
# 4 0  8  8   8
# 5 0  0  0   12
# 6 13 13 13  13
# 7 0  0  14  14
#최대적재

n, k = map(int, input().split())
table = [0] *  (k+1)
            
for _ in range(n): #물건개수
    w, v = map(int, input().split())
    if w > k:
        continue
    for j in range(k, 0, -1): # 거꾸로 해야 weight 필요없는거 작성안함 (ex) 7일때는 걍 넘어가, 4일때 3인거 만나면 그때 7 업데이트, 0은 안써요
        if j + w <= k and table[j] != 0:
            table[j + w] = max(table[j+w], table[j] + v)
    table[w] = max(table[w], v)

print(max(table))
        
            

# 2D

# n, k = map(int, input().split())

# dp = [[0] * (k + 1) for _ in range(n + 1)] # n 물건개수, k 최대적재
# for i in range(1, n + 1):
#     weight, value = map(int, input().split())
#     for j in range(1, k + 1):
#         if j < weight:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
# print(dp)