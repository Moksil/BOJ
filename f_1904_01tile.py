dp = [[0 for _ in range(1000001)] for _ in range(1000001)]

for value in range(1000001):
	for partition in range(1000001):
		if value == 1:
			dp[value][partition] = partition % 15746
		elif partition == 1:
			dp[value][partition] = value % 15746
		else:
			dp[value][partition] = sum(dp[value - 1])

N = int(input())

limit = N // 2
sum = 0

for num_of_00 in range(limit + 1):
	num_of_1 = N - (num_of_00 * 2)
	if num_of_00 == 0 or num_of_1 == 0:
		sum += 1
	else:
		sum += dp[num_of_00][num_of_1 + 1]

print(sum)