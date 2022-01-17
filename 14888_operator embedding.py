def check(p_list, oper_list):
	check_list = []
	for cpy in oper_list:
		check_list.append(cpy)
	for val in p_list:
		check_list[val] -= 1
		if check_list[val] < 0:
			return False
	return True
	

def dfs(oper_lst, promising, blank, N, depth):
	if depth == N - 1:
		promise_lst = []
		for cpy in blank:
			promise_lst.append(cpy)
		promising.append(promise_lst)
		return True
	ret = False
	for i in range(4):
		blank.append(i)
		if check(blank, oper_lst):
			if dfs(oper_lst, promising, blank, N, depth + 1):
				ret = True 
			else:
				ret = False
		blank.pop(-1)
	return ret

def calc_equation(input_list, promising_set):
	result = input_list[0]
	for idx in range(len(promising_set)):
		if promising_set[idx] == 0:
			result = result + input_list[idx + 1]
		if promising_set[idx] == 1:
			result = result - input_list[idx + 1]
		if promising_set[idx] == 2:
			result = result * input_list[idx + 1]
		if promising_set[idx] == 3:
			if result < 0:
				result = -((-result) // input_list[idx + 1])
			else:
				result = result // input_list[idx + 1]
	return result

N = int(input())
input_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))
# ([0] : +), ([1] : -), ([2] : *), ([3] : /)

promising = []
blank = []
dfs(oper_lst, promising, blank, N, 0)
min = calc_equation(input_lst, promising[0])
max = min

for promising_set in promising[1: ]:
	val = calc_equation(input_lst, promising_set)
	if val < min:
		min = val
	if val > max:
		max = val

print(max)
print(min)