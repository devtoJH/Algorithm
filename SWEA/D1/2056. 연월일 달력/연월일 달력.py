import datetime
T = int(input())
for t in range(1, T+1):
    num = input()
    year, month, day = num[:4], num[4:6], num[6:]
    try:
        datetime.date(int(year), int(month), int(day))
        print(f"#{t} {year}/{month}/{day}")
    except:
        print(f"#{t} -1")