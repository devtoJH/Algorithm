def solution(num_list):
    answer = []
    
    cnt1 = 0 # 홀수
    cnt2 = 0 # 짝수
    for i in num_list:
        if i % 2 == 0:
            cnt2 += 1
        else:
            cnt1 += 1
    answer = [cnt2, cnt1]
    return answer