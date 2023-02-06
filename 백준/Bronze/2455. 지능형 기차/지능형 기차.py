cnt = 0
in_train = []

for _ in range(4):
    out_people, in_people = map(int, input().split())
    cnt += in_people
    cnt -= out_people
    in_train.append(cnt)
print(max(in_train))