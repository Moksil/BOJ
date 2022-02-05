def w(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	if a > 20 or b > 20 or c > 20:
		return w(20, 20, 20)
	ans = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
	for i in range(0, 21):
		for j in range(0, 21):
			for k in range(0, 21):
				if i == 0 or j == 0 or k == 0:
					ans[i][j][k] = 1
					continue
				if i < j and j < k:
					ans[i][j][k] = ans[i][j][k - 1] + ans[i][j - 1][k - 1] - ans[i][j - 1][k]
					continue
				else:
					ans[i][j][k] = ans[i - 1][j][k] + ans[i - 1][j - 1][k] + ans[i - 1][j][k - 1] - ans[i - 1][j - 1][k - 1]
	return ans[a][b][c]

input_list = []
while (1):
	a, b, c = map(int, input().split())
	if a == -1 and b == -1 and c == -1:
		break
	input_list.append([a, b, c])

for input_set in input_list:
	print("w({}, {}, {}) = {}".format(input_set[0], input_set[1], input_set[2], w(input_set[0], input_set[1], input_set[2])))




# Better Solution
"""
import sys
input = sys.stdin.readline

dp = {}

def w(a, b, c):
	if (a, b, c) in dp.keys():
		return dp[(a, b, c)]
	else:
		if a <= 0 or b <= 0 or c <= 0: return 1
		elif a > 20 or b > 20 or c > 20: return w(20, 20, 20)
		else:
			dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
		return dp[(a, b, c)]	

while True:
	a, b, c = map(int, input().split())
	if a == b == c == -1: break
	print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
"""
"""

<review> : maybe 2 or more
"""
