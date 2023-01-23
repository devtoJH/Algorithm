string = input().lower()
string_list = list(set(string))
#print(string_list)
cnt = []

for i in string_list:
    count = string.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(string_list[(cnt.index(max(cnt)))].upper())