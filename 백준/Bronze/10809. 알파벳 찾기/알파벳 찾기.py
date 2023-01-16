string = input()
alphabet = list(range(97, 123))
for i in alphabet:
    print(string.find(chr(i)), end=' ')