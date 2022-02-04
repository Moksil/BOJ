N = int(input())
input_list = []
for _ in range(N):
	input_list.append(int(input()))
ans_list = [(1, 0), (0, 1)]

max_val = max(input_list) + 1

for i in range(2, max_val):
	ans_list.append((ans_list[i - 1][0] + ans_list[i - 2][0], ans_list[i - 1][1] + ans_list[i - 2][1]))

for val in input_list:
	zero_call, one_call = ans_list[val][0], ans_list[val][1]
	print(zero_call, one_call)

"""

<review> : maybe 2 or more
"""
