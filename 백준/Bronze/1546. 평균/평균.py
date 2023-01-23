N = int(input())
score = list(map(int, input().split()))
M = max(score)
score_list = []
for i in score:
    score_list.append(i/M*100)
print(sum(score_list)/N)