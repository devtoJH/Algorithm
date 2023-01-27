import sys
input = sys.stdin.readline
N = int(input())
word_list = []
set_word = set()

for n in range(N):
    word = input().strip()
    set_word.add(word)

for i in set_word:
    word_list.append(i)
    word_list.sort()
    
word_list.sort(key=len) 

for j in word_list:
    print(j)