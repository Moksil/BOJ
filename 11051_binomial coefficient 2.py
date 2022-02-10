# Refined Solution
# first submitted solution is in bottom of this file

N, K = map(int, input().split())

dp = [[0 for _ in range(row)] for row in range(1, 1002)]

for n in range(len(dp)):
	for k in range(n + 1):
		if k == 0 or k == n:
			dp[n][k] = 1
		else:
			dp[n][k] = (dp[n - 1][k - 1] + dp[n - 1][k]) % 10007

print(dp[N][K])

# [실버1] 11051 - 이항 계수 2
# 220210_#1 파이썬엔 정수 제한이 없지롱
"""
comment

N과 K의 범위가 (1 <= N <= 1,000, 0 <= K <= N)로 주어졌다.
N = 1000, K = 500의 이항계수는 약 300자리의 수가 나온다
python3 에서 10007로 나눈 나머지는 %연산으로 바로 계산 가능.

하지만 int_max를 상정하고 이항계수의 수학적 개념 파스칼의 삼각형을 dp로 구현했다.
항상 dp문제를 풀때는 인덱스를 정교하게 처리해야한다.

<review> : maybe 4 or more
"""

# first submitted solution
"""
N, K = map(int, input().split())

result = 1

for n in range(N, N - K, -1):
	result *= n
for k in range(K, 1, -1):
	result //= k

print(result % 10007)
"""