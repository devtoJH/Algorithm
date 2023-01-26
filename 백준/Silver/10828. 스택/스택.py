import sys
input = sys.stdin.readline
N = int(input())
stack = []

for n in range(N):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command == ['pop']:
        if len(stack) == 0:
            print('-1')
        elif len(stack) > 0:
            print(stack.pop(-1))
    elif command == ['size']:
        print(len(stack))
    elif command == ['empty']:
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif command == ['top']:
        if len(stack) > 0:
            print(stack[-1])
        elif len(stack) == 0:
            print('-1')