T = int(input())
for t in range(T):
    string = input()
    print(f'{string[0]}{string[len(string)-1:len(string)]}')