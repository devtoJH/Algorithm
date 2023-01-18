string = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabet:
    string = string.replace(i, '.')
print(len(string))