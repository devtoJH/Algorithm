N = int(input()) # 손님의 수
pc_customer = list(map(int, input().split())) # 앉고 싶어하는 자리
pc = [] # 컴퓨터 자리 수
pc_refuse = 0 # 거절당한 사람

for i in range(N):
    if pc_customer[i] in pc:
        pc_refuse += 1
    else:
        pc.append(pc_customer[i])
print(pc_refuse)