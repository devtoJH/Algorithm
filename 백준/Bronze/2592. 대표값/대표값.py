num_list = [int(input()) for _ in range(10)]
print(sum(num_list)//10)
print(max(num_list, key = num_list.count))