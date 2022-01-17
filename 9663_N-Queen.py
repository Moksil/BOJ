def tracking(lst, N, row):
	ret = 0
	if row == N:
		return 1
	remain = [i for i in range(N)]
	for i in range(row):
		remain.remove(lst[i])
	for i in remain:
		for j in range(row):
			if lst[j] == i or abs(i - lst[j]) == row - j:
				break
		else:
			lst[row] = i
			ret += tracking(lst, N, row + 1)
	return ret

N = int(input())
lst = [0] * N

print(tracking(lst, N, 0))


# result : KO - timeover