N = int(input())

lst = list(map(int, input().split()))
lst.sort()

sum = 0
wating = 0
for time in lst:
	sum += wating + time
	wating += time

print(sum)

# 그리디에서 정렬은 해결사?
"""
[실버3]
쉬운 그리디 문제라서 금방 풀림.
총합을 계산할 때 누적된 wating이 중복으로 더해지기 때문에 전체 wating을 줄이려면 낮은 수부터 실행되야함.
직관적으로 구현 방법이 떠올랐지만, 실행 없이 결과를 예측해보는 연습이 더 필요 함.

python의 reduce + lambda를 통해서 풀이하려 했지만 오히려 가독성을 해치는 현학적 풀이라고 생각하여 포기.
"""