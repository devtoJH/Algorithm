N = int(input())

# N번째
cnt = 0
movie_num = 666

while True:
    # 숫자에 666이 있는지?
    if '666' in str(movie_num):
        cnt += 1

    # 무한반복문을 종료할 조건
    # N번째 나온 영화 이름을 찾을 때
    if cnt == N:
        break

    movie_num += 1

# N번째 영화 이름 출력
print(movie_num)