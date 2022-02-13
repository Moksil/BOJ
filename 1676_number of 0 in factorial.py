# ---------- 입력 ---------- #
N = int(input())
# ------------------------- #

# --- solution 1 : int_max 무시한 풀이 --- #

"""
from functools import reduce

def fact(num):
	return reduce(lambda x, y : x * y, range(1, num + 1), 1)

to_str = str(fact(N))

for idx, ch in enumerate(reversed(to_str)):
	if ch != '0':
		print(idx)
		break
"""
# -------------------------------------- #

# --- solution 2 : int_max 고려한 풀이 --- #
# """
def count_10_factor(num):
	factor_of_5 = 0
	for n in range(1, num + 1):
		while (n % 5 == 0):
			n //= 5
			factor_of_5 += 1
	print(factor_of_5)

count_10_factor(N)
# """
# -------------------------------------- #


# [실버4] 1676 - 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676
# 220212_#2 int_max 따위 파이썬에선 전혀 문제가 없지롱
"""
어렵지 않은 문제.
입력이 500! 까지 가능하기 때문에 int_max를 넘는 범위를 어떻게 handling할 것인지 생각 해봐야함.
물론 파이썬에서는 그런거 안해도 됨 ㅎㅎ

고려해서 풀어야 한다면 함수를 별도로 만들어서 factorial 값을 구하지 않고,
10으로 나누어 떨어질 때 마다 count를 두어 계산하는 방법을 생각해 볼 수 있음.
factorial 계산의 특성상 2 factor는 매우 많고 5 factor보다 항상 많음.
5 factor의 갯수가 10으로 나누어 떨어지게 되는 횟수

두가지 풀이 모두 정답.

<review> : except problem, only comment
"""