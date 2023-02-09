T = int(input())

for t in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    A = p * w
    B = q
    if r < w:
        B = q + ((w - r) * s)
    
    if A > B:
        print(f'#{t} {B}')
    else:
        print(f'#{t} {A}')