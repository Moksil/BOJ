N = int(input())

input_lst = [int(input()) for _ in range(N)]
lst = list(map(int, "01112234579"))

for i in range(11, max(input_lst) + 1):
	lst.append(lst[i - 1] + lst[i - 5])

for test_case in input_lst:
	print(lst[test_case])

# [실버3] 9461 - 파도반수열
# https://www.acmicpc.net/problem/9461
# 220215_#1 DP문제는 대부분 dps로도 풀릴걸?

"""
쉬운 문제.

피보나치 수열과 비슷한 방식으로 푸는 수열문제
그림을 보고 규칙을 찾아내면 쉽게 풀 수 있는 문제였다.

<review> : except problem, only comment
"""