import math

def solution(price):
    if 300000 > price >= 100000:
        answer = int(price - (price * 0.05))
    if 500000 > price >= 300000:
        answer = int(price - (price * 0.1))
    if price >= 500000:
        answer = int(price - (price * 0.2))
    if price < 100000:
        answer = price
    
    return answer