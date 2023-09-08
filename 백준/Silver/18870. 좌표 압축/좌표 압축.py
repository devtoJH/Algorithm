import sys
input = sys.stdin.readline

n = int(input())
points = list(map(int, input().split()))
arr = sorted(set(points))
dic = {arr[i]:i for i in range(len(arr))} # arr의 길이만큼 arr배열의 요소에 추가

for i in points:
    print(dic[i], end = ' ')