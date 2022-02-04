a, b = map(int, input().split())
lower = min(a, b)

while not(a == 0 or b == 0):
	if (a == lower) and (b % a == 0):
		print("factor")
	elif (b == lower) and (a % b == 0):
		print("multiple")
	else:
		print("neither")
	a, b = map(int, input().split())
	lower = min(a, b)

# [브론즈3] 5086 - 배수와 약수
# 220204_#4 배수 약수 나올 때 devided zero는 한 번 생각해보자
"""
쉬운 문제여서 금방 풀렸다.
이 문제에서는 입력에 자연수가 주어져 devided zero는 무시해도 되는 경우였지만,
배수 약수 문제에서는 해당 경우를 생각해보면 오류를 줄일 수 있을 것 같다.

<review> : except code, only comment
"""