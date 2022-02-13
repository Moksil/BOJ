T = int(input())

output_lst = []
for _ in range(T):
	N = int(input())
	sol = 1
	input_dict = {}
	for _ in range(N):
		input_set = input().split()
		if input_set[1] not in input_dict:
			input_dict[input_set[1]] = 1
		else:
			input_dict[input_set[1]] += 1
	for item_type in input_dict:
		sol *= input_dict[item_type] + 1
	output_lst.append(sol - 1)

for sol in output_lst:
	print(sol)

# [실버3] 9375 - 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
# 220212_#1 딕셔너리는 매우 강력ㅋ. 이 맛에 파이썬 쓰지
"""
쉬운 경우의 수 문제.
dict자료형을 사용하여 직접 counter를 만들거나 라이브러리 counter를 사용하여 풀면 쉽게 풀림.

<review> : except problem, only comment
"""