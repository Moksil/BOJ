a, b = map(int, input().split())

limit = min(a, b) + 1
gcd = 1
for i in range(2, limit):
	if a % i == 0 and b % i == 0:
		gcd = i
	
print(gcd)
print(a * b // gcd)

# [실버5] 2609 - 최대공약수와 최소공배수
# 220205_#1 정수론 문제는 몇 개 안되는 사전지식으로 짧은코드, 쉬운풀이를 만들 수 있다.

# better Solution
"""
유클리드 호제법 풀이, 정수론 문제 기본 개념. 암기.

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
"""

"""
최대공약수, 최소공배수 문제는 둘중에 하나만 구하면 됨.
최소공배수는 (최대공약수 * 두 수의 곱)으로, 최대공약수는 (최소공배수 // 두 수의 곱) 쉽게 구해짐.
유클리드 호제법 풀이는 기본 개념. 외우기!!

<review> : except problem, only comment
"""