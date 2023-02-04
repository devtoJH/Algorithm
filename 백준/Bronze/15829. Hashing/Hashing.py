L = int(input())
str_L = input()

asc = []
hash_L = []

for i in str_L:
    asc.append(ord(i))
    #print(asc_num, end=' ')

for j in range(len(asc)):
    # print(j)
    hash_L.append((asc[j] - 96) * (31 ** j))

print(sum(hash_L))