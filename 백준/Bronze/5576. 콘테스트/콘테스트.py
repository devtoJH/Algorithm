W_score_list = []
K_score_list = []

for _ in range(10):
    W_score = int(input())
    W_score_list.append(W_score)
    W_score_list.sort()

for _ in range(10):
    K_score = int(input())
    K_score_list.append(K_score)
    K_score_list.sort()

print(W_score_list[7] + W_score_list[8] + W_score_list[9], K_score_list[7] + K_score_list[8] + K_score_list[9])