def solution(my_string, n):
    my_string=list(my_string)
    for i in range(0, len(my_string)):
        my_string[i] = my_string[i] * n
    answer = ''.join(my_string)
    return answer