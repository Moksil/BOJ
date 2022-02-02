N, K = map(int, input().split())
coin_list = []
for _ in range(N):
	coin_list.append(int(input()))

ans = 0
for coin in reversed(coin_list):
	if coin > K:
		continue
	while K >= coin and K != 0:
		K -= coin
		ans += 1
	if K == 0:
		break
print(ans)

# 간단한 그리디 문제.
# 조건에 따라 입력에서 동전의 액면금액이 오름차순으로 주어 짐
# 조건 중 입력되는 동전의 액면금액은 바로 이전 액면금액의 배수여야 한다는 조건이 그리디로 풀 수 있는 이유를 설명.
# line 8의 조건문 부등호에 등호 넣어줘서 첫트 실패. 이후 수정.