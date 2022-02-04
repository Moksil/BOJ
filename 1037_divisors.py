N = int(input())
lst = list(map(int, input().split()))

if 2 in lst:
	print(2 * max(lst))
else:
	print(min(lst) * max(lst))

# [실버5] 1037 - 약수
# 220204_#5약수 배수 소수 문제에서는 간단한 수학개념이 코드를 훨씬 쉽게 만들어준다.
"""
쉬운 문제.
input으로 모든 약수가 주어지기 때문에 짝수는 항상 2를 약수로 가진다는 개념만 빨리 떠오르면 바로 풀림.

<review> : except code, only comment
"""
