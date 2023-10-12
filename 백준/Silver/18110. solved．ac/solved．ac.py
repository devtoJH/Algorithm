import sys
 
def round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)
 
input = sys.stdin.readline
n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    m = round(n * 0.15)
    print(round(sum(arr[m:-m] if m else arr) / (n - 2 * m)))
else:
    print(0)