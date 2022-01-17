from itertools import combinations

def calc_stat_sum(stat_table, team):
	sum = 0
	for i in team:
		for j in team:
			sum += stat_table[i][j]
	return sum

N = int(input())
stat_table = []
for _ in range(N):
	stat_table.append(list(map(int, input().split())))

t_list = list(combinations(list(range(N)), N // 2))

min = abs(calc_stat_sum(stat_table, t_list[0]) - calc_stat_sum(stat_table, t_list[-1]))
for idx in range(len(t_list) // 2):
	val = abs(calc_stat_sum(stat_table, t_list[idx]) - calc_stat_sum(stat_table, t_list[-1 -idx]))
	if min > val:
		min = val

print(min)
