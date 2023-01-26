T = int(input())
Q = 25
D = 10
N = 5
P = 1
for t in range(T):
    C = int(input())
    q = C // Q
    d = (C % Q) // D
    n = ((C % Q) % D) // N
    p = (((C % Q) % D) % N) // P
    print(q, d, n, p)