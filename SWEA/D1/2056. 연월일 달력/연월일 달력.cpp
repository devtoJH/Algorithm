T = int(input())
for t in range(1, T+1):
    n = input()
    year = n[0:4]
    month = n[4:6]
    day = n[6:8]

    if month == '00' or month > '12':
        print(f'#{t} -1')
    else:
        # print('1')
        if month == '02':
            #print('1')
            if day > '28':
                print(f'#{t} -1')
            else:
                print(f'#{t} {year}/{month}/{day}')
        else:
            print(f'#{t} {year}/{month}/{day}')