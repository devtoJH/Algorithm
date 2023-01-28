N, M = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for n in range(N):
    for i in range(n+1, N):
        for j in range(i+1, N):
            card_sum = card[n] + card[i] + card[j]
            if card_sum <= M:
                result = max(result, card_sum)
print(result)