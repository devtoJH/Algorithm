n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
  L, H = 0, n-1
  while True:
    if L > H:
      print('0 ', end='')
      break
    m = (L + H) // 2
    if n_list[m] == i:
      print('1 ', end='')
      break
    elif n_list[m] > i:
      H = m - 1
    else:
      L = m + 1