N, K = map(int, input().split())

result = 1

for n in range(N, N - K, -1):
	result *= n
for k in range(K, 1, -1):
	result //= k

print(result)

# [브론즈1] 11050 - 이항 계수1
# 220208_#1 기본적인 수학 개념은 알아야 한다.
"""
어려운 개념은 아닌데 이항계수가 뭔지는 알아야 푸는 문제.
이런 문제가 코테에 나올 리는 없겠지만 충분히 응용 가능함. 다음 문제 11051이 진짜 이항계수 문제.

<review> : except problem, only comment
"""