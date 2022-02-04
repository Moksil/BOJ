N = int(input())

distance_lst = list(map(int, input().split()))
price_lst = list(map(int, input().split()))

sum = 0
del price_lst[-1]

puel_price = price_lst[0]

for idx, price in enumerate(price_lst):
	if puel_price > price:
		puel_price = price
	sum += puel_price * distance_lst[idx]

print(sum)

# [실버4] 13305 - 주유소
# 220204_#3 입력에서 정보가 다 주어지면 파생되는 정보를 활용할 수 있다.
"""
계산하기 전에 거리와 가격의 모든 값이 주어지기 때문에
싼 가격이 올 때 가격을 변경해주면 됨.
연료 저장고가 무한하다는 것이 힌트.

<review> : except code, only comment
"""