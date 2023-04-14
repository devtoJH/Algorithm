def solution(age):
    answer = ''
    pg_962 = 'abcdefghij'
    for i in str(age):
        answer += pg_962[int(i)]
    return answer