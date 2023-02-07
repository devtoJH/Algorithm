# 8방향 델타값
direction = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

k, s, n = input().split()

# 킹과 돌의 위치
kx, ky = 8 - int(k[1]), ord(k[0]) - 65 # king x, y
sx, sy = 8 - int(s[1]), ord(s[0]) - 65 # stone x, y
#print(kx, ky, sx, sy)

for _ in range(int(n)):
    move = input().strip()
    # 킹이 움직이는 방향
    dx, dy = direction[move]
    #print(direction[move])

    # 킹이 체스판 범위를 벗어나는 경우 해당 이동 건너뜀
    if not (0 <= kx+dx < 8 and 0 <= ky+dy < 8):
        continue

    kx += dx
    ky += dy

    if (kx, ky) == (sx, sy):
        # 돌이 체스판 범위를 벗어나는 경우 해당 이동 건너뜀
        if not (0 <= sx+dx < 8 and 0 <= sy+dy < 8):
        	# 킹의 움직임 되돌리기
            kx -= dx
            ky -= dy
            continue

        sx += dx
        sy += dy
       
print(chr(ord("A")+ky)+str(8-kx))
print(chr(ord("A")+sy)+str(8-sx))