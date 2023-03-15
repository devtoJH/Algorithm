a_x, a_y, a_z = map(int, input().split())
b_x, b_y, b_z = map(int, input().split())
print(b_x - a_z, b_y // a_y, b_z - a_x)