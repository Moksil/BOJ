# Refined Solution
# first submited solution is in bottom of this file

from functools import reduce

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def get_divisor(n):
	front_lst = []
	back_lst = []
	for i in range(2, int(n ** (0.5)) + 1):
		if n % i == 0:
			front_lst.append(i)
			back_lst.append(n // i)
	if int(n ** 0.5) in back_lst:
		back_lst.remove(int(n ** 0.5))
	return front_lst + list(reversed(back_lst))

N = int(input())
input_lst = sorted([int(input()) for _ in range(N)])

# sol 1 : 좀 더 세세한 조건검사, 수행시간 약간 더 소모함.
mapped_lst = list(map(lambda x: x - input_lst[0], input_lst[1:]))
GCD = reduce(gcd, mapped_lst)

# sol 2 : 대략적인 조건검사이지만, 수행시간이 좀 더 짧음
"""
if len(input_lst) == 2:
	GCD = input_lst[-1] - input_lst[0]
else:
	GCD = gcd(input_lst[-2] - input_lst[0], input_lst[-1] - input_lst[0])
"""
# -> input case에 따라 수행시간은 달라질 수 있음. sol 1이 좀 더 일반적인 solution

divisor_lst = get_divisor(GCD)
divisor_lst.append(GCD)

solution_lst = [i for i in divisor_lst if GCD % i == 0]

for i in solution_lst:
	if i != solution_lst[-1]:
		print(i, end = " ")
	else:
		print(i)



# [골드5] - 검문
# 220209_#1 정수론, 나머지, 문제에서 gcd를 활용한 핵심을 찾아보자.
"""
시간제한으로 이틀에 거쳐 풀이한 문제.
풀기 위한 로직은 어렵지 않으나 시간복잡도를 줄이는 방법을 생각 해 내는 것이 관건.

최소 입력 값 보다 큰 값이 정답에 포함되려면 최소 입력 값보다 큰 입력의 나머지가 모두 최소 입력 값이 되어야 함.
항상 값이 존재하는 입력이 주어지는 조건이 있으므로,
나머지 입력에 최소 입력 값을 뺀 모든 값들의 공약수를 정답에 활용하는 것이 포인트.
* 세 수 이상의 최대공약수를 구하는 방법은 두 수의 최대공약수를 먼저 구해서,
두 수의 최대 공약수와 남은 숫자의 최대공약수를 구하면 됨.
최소 입력 값을 제외한 나머지 모든 입력의 최대공약수를 구하는 방법으로 reduce를 활용. -> 아래에 reduce() 개념 정리

최소 입력 값을 뺀 리스트들의 최대공약수를 구해서,
구해진 최대공약수와 구해진 최대공약수의 약수들의 리스트만을 조건과 만족하는지를 확인하면 시간복잡도를 매우 줄일 수 있음.

reduce(function, iterable)
2개의 인자를 받는 function을 사용하여,
iterable의 원소의 첫번째부터 누적적으로 적용하여 단일 값으로 변환하여 반환.
iterable이 단일원소를 가지고 있을 경우 해당 원소가 값으로 반환
->
    for element in iterable:
        value = function(value, element)

<review> : maybe 5 or more, import comment!
"""

"""
reduce() 예제코드 - factorial 함수.

from functools import reduce

def factorial_using_reduce(num):
	if num == 0:
		return 1
	return reduce(lambda x, y : x * y, range(1, num + 1))
"""

# first submited solution
"""
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
"""