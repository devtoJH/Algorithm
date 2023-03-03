calendar = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

for t in range(1, int(input())+1):
    cd = tuple(map(int, input().split()))
    result = 0 - cd[1] - (calendar[str(cd[2])] - cd[3]) + 1
    for i in range(cd[0], cd[2]+1):
        result += calendar[str(i)]
    print(f"#{t} {result}")