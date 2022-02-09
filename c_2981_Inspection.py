import math

def get_divisor_lst(num):
	divisor_lst = []
	limit = int(math.sqrt(num)) + 1
	for i in range(2, limit):
		if num % i == 0:
			divisor_lst.append(i)
			divisor_lst.append(num // i)
	divisor_lst = sorted(list(set(divisor_lst)))
	return divisor_lst

def get_gcd(a, b):
	if a == 0 or b == 0:
		return 1
	while b > 0:
		a, b = b, a % b
	return a

N = int(input())
input_lst = []

for _ in range(N):
	input_lst.append(int(input()))

input_lst.sort()
output_lst = []

gcd = get_gcd(input_lst[-2] - input_lst[0], input_lst[-1] - input_lst[0])
if gcd == 1:
	divisor_list = get_divisor_lst(input_lst[-1] - input_lst[0])
	divisor_list.append(input_lst[-1] - input_lst[0])
else:
	divisor_list = get_divisor_lst(gcd)
	divisor_list.append(gcd)

for M in divisor_list:
	for num in input_lst:
		if num % M != input_lst[0] % M:
			break
	else:
		output_lst.append(M)

for i in output_lst:
	if i != output_lst[-1]:
		print(i, end=' ')
	else :
		print(i)