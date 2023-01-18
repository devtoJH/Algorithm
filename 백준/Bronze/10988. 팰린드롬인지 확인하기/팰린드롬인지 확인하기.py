string = input()

if string[:len(string)+1] == string[::-1]:
    print('1')
else:
    print('0')