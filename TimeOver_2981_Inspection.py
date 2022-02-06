import math

def get_divisor_lst(num):
	divisor_lst = []
	limit = int(math.sqrt(num)) + 1
	for i in range(2, limit):
		if num % i == 0:
			divisor_lst.append(i)
			divisor_lst.append(num // i)
	divisor_lst.sort()
	return divisor_lst


N = int(input())
input_lst = []

for _ in range(N):
	input_lst.append(int(input()))

input_lst.sort()
output_lst = []

for M in range(2, input_lst[0] + 1):
	remainder = input_lst[0] % M
	for num in input_lst:
		if num % M != remainder:
			break
	else:
		output_lst.append(M)


for val in input_lst:
	if val == input_lst[0]:
		continue
	divisor_list = get_divisor_lst(val - input_lst[0])
	for M in divisor_list:
		for num in input_lst:
			if num % M != input_lst[0]:
				break
		else:
			output_lst.append(M)
	
output_lst = list(set(output_lst))

for i in output_lst:
	if i != output_lst[-1]:
		print(i, end=' ')
	else :
		print(i)



# dfs 백트래킹으로 탐색?
# min % i
# min보다 큰 숫자로 나누면 값은 항상 min
# 2부터 max까지 해야함.