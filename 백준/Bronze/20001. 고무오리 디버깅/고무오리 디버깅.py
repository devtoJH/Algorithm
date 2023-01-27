string = input()
duck_list = []

while string != '고무오리 디버깅 끝':
    if string == '문제':
        duck_list.append(string)
    elif string == '고무오리':
        if '문제' in duck_list:
            duck_list.pop()
        elif '문제' not in duck_list:
            duck_list.append('문제')
            duck_list.append('문제')
    string = input()

if '문제' in duck_list:
    print('힝구')
else:
    print('고무오리야 사랑해')