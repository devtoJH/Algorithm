N = int(input())
a = list(input())
a_len = len(a)
             
for i in range(N - 1):
    word = list(input())
    for j in range(a_len):
        if a[j] != word[j]:
            a[j] = '?'

print(''.join(a))