M = int(input())
cup = [1, 2, 3]

for _ in range(M):
    X, Y = map(int, input().split())

    move_cup_x = cup.index(X)
    move_cup_y = cup.index(Y)

    cup[move_cup_x], cup[move_cup_y] = cup[move_cup_y], cup[move_cup_x]

print(cup[0])