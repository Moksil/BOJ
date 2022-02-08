def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

N = int(input())
input_lst = list(map(int, input().split()))

for i in input_lst[1 :]:
	gcd_i = gcd(input_lst[0], i)
	print("{}/{}".format(input_lst[0] // gcd_i, i // gcd_i))

# [실버3] 3036 - 링
# 220206_#1 배수, 약수 문제에 최대공약수를 활용
"""
쉬운문제.
문제의 내용은 간단함. 기약분수 표현을 어떻게 만들지에 대한 고민 -> 최대공약수 연산으로 해결.

<review> : except problem, only comment
"""