exp = input()

op_lst = ['+']
for idx in range(len(exp)):
	if exp[idx] == '+' or exp[idx] == '-':
		op_lst.append(exp[idx])

lst = list(map(int, exp.replace('-', '+').split('+')))

sum = 0
flag = 1

for i in range(len(lst)):
	if flag == 1 and op_lst[i] == '-':
		flag = -1
	sum += flag * lst[i]

print(sum)

# [실버2] 1541 - 잃어버린 괄호
# 220204_#2 문제를 완전히 이해하고 다양한 방법으로 생각해보면 쉬운 해법이 나온다.
"""
난이도에 비해 쉬운 문제.
결과는 최소 값을 출력하는 것.
'-'가 한 번이라도 나온 이후부터는 모두 빼기 가능하다는 것이 key point

2개 이상의 구분자로 split을 수행하는 트릭 사용함.
모든 구분자를 replace를 사용하여 한가지 구분자로 통일하고 통일된 구분자로 .split()수행

<review> : except code, only comment
"""