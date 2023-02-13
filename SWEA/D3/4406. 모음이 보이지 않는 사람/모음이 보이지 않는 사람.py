T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']
for t in range(1, T+1):
    string = input()
    string_list = []

    for i in string:
        string_list.append(i)
    
    for j in range(len(string_list)):
        for k in vowel:
            if k in string_list:
                string_list.remove(k)
    a = ''.join(string_list)
    print(f'#{t} {a}')