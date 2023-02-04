T = int(input())

floor_list = []

for t in range(T):
    k = int(input()) # 층
    n = int(input()) # 호

    # 0층의 i호는 i명 거주
    people = [i for i in range(1, n+1)]
    #print(people)

    for j in range(k):
        for m in range(1, n):
            people[m] += people[m-1]
    
    print(people[-1])