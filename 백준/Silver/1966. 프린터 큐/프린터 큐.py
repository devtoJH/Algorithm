import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    
    priority = list(map(int, sys.stdin.readline().split()))
    
    idx = [i for i in range(n)]
    cnt = 0
    
    while True:
        if priority[0] == max(priority):
            cnt += 1
            if idx[0] == m:
                print(cnt)
                break
            else:
                # del : 해당 변수들을 삭제
                del priority[0]
                del idx[0]
        else:
            priority.append(priority[0])
            del priority[0]
            idx.append(idx[0])
            del idx[0]