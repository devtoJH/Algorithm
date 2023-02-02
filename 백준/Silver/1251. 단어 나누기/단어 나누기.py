word = input()
word_list = []

# 완전 탐색
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            word_reverse = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            word_list.append(word_reverse)

# 사전 순으로 나열
word_list.sort()
print(word_list[0])
