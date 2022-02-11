# ---------- 입력 ---------- #

T = int(input())
input_lst = [list(map(int, input().split())) for _ in range(T)]

# ------------------------- #


# ----- solution 1 : DFS ----- #
"""
# def bfs(n, m):
# 	sol = 0
# 	if n == m:
# 		return 1
# 	elif n == 1:
# 		return m
# 	for select in range(1, m - n + 2):
# 		sol += bfs(n - 1, m - select)
# 	return sol

for i in input_lst:
	print(bfs(i[0], i[1]))
"""
# ---------------------------- # -> TIMEOVER

# ----- solution 2 : DP ----- #
"""
dp = [[0 for west in range(east + 1)] for east in range(31)]
dp[1][1] = 1
for M in range(1, len(dp)):
	for N in range(1, M + 1):
		if N == 1:
			dp[M][N] = M
		if N == M:
			dp[M][N] = 1
		else:
			for select in range(1, M - N + 2):
				dp[M][N] += dp[M - select][N - 1]

for i in input_lst:
	print(dp[i[1]][i[0]])
"""
# --------------------------- #


# ----- solution 3 : 조합 ----- #
from functools import reduce

def fact(num):
	return reduce(lambda x, y : x * y, range(2, num + 1), 1)

def comb(a, b):
	return fact(a) // (fact(a - b) * fact(b))

for i in input_lst:
	print(comb(i[1], i[0]))
# ---------------------------- #


# [OON] 1010 - 다리 놓기
# 220211_#1 경우의 수 문제는 다양한 방법으로 풀 수 있다.
"""
조합을 사용해서 문제를 풀면 간단히 풀리는 문제인데 dfs가 먼저 생각났다.
1. dfs는 timeover.

2. 그 다음 생각 난 방법이 dp를 통한 풀이.
dp는 잘 짜려면 인덱스 정교하게 다루는 방법을 꾸준히 연습해야 할 것 같다.
아직 여러번 시도해야한다.

3. 마지막으로 가장 간단한 조합을 통한 풀이가 떠올랐다.
난이도를 보면 이 방법을 이용한 풀이가 가장 일반적인 풀이라고 생각되는데 왜 이게 늦게 떠올랐지?
괜히 고생하긴 했는데 덕분에 다양한 방법으로 풀면서 좋은 연습이 된 것 같다.

reduce를 통해 factorial을 1줄짜리 함수로 구현할 수 있다.
factorial함수를 구현하면 조합도 1줄로 구현할 수 있다.
리스트의 원소 조합을 필요로 하는게 아닌 단순 숫자를 구하는 조합 문제라면 직접 구현하는 방법이 썩 나쁘지 않다.
factorial, combination 간단 구현 코드를 익혀두자.

<review> : except problem, comment and code
"""