def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

T = int(input())

for _ in range(T):
	test_case = list(map(int, input().split()))
	print(lcm(test_case[0], test_case[1]))

# [실버5] 2609 - 최소공배수
# 220205_#2 유클리드 호제법 쓱쓱싹싹
"""
def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

유클리드 호제법 알면 30초컷

<review> : except problem, only comment
"""