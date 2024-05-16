num_cards, des = input().split()
num_cards = int(num_cards)
des = int(des)

arr = list(map(int, input().split()))

a,b,c = 0,0,0
answer = []

for i in range(0, num_cards-2):
    for j in range(1, num_cards-1):
        for k in range(2, num_cards):
            if i != j and j != k and i != k:
                a = arr[i]
                b = arr[j]
                c = arr[k]
                sum = a + b + c

                if sum <= des:
                    answer.append(sum)


print(max(answer))

