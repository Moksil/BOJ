N = int(input())

time_table = []

for _ in range(N):
	time_set = list(map(int, input().split()))
	time_table.append(time_set)

time_table.sort(key = lambda x : (x[1], x[0]))

sol = 0
for i in range(len(time_table)):
	if i == 0:
		sol += 1
		occupied = time_table[0][1]
	elif occupied <= time_table[i][0]:
		sol += 1
		occupied = time_table[i][1]

print(sol)

# 220204 정렬은 생각지도 못했던 문제를 해결해줄 수 있다. 
"""
문제풀이에 시간 굉장히 오래 걸림.
입력 검증 함수를 통해 입력을 줄이는 방법으로 풀었다가 시간초과.

시작하는 시간보다 끝나는 시간이 주요했음. 하지만 시작시간 고려 없이 풀면 오답.
"종료시간 기준 오름차순 정렬 -> 시작시간 기준 오름차순 정렬" 로 해결
종료시간 기준 오름차순 정렬만으로 풀릴 것 같지만 오답.
반례 > [3 3], [0 3] 의 경우 2차 기준으로 시작시간 오름차순 정렬되어 [0, 3], [3, 3]이 되면,
두 슬롯 모두 사용 가능으로 인식하지만, 정렬 없이 사용되면 [3,3]만 사용 가능한 것으로 인식하게 됨.

cf. 정렬방법 sorted & .sort() 
	- sorted() : 내장 함수. 인자로 전달된 리스트 유지하고 정렬된 리스트 return.
	- .sort() : list 제공 함수. return 값 반환 없이 내부 정렬 실행.

cf. reversed() & .reverse()
	- reversed() : 내장 함수. 인자로 전달된 리스트 유지하고 역순 리스트 return.
	- .reverse() : list 제공 함수. tuple, dict에서 사용 불가. 값 반환 없이 내부 역순 정렬.

lambda 사용하여 2차원 이상 배열 우선순위 지정하여 정렬 가능.
lambda 사용 법 : 이름 없는 함수를 생성. [lambda 매개변수 : return]
정렬에서의 응용 : 정렬 sorted(), .sort()에서 key = <function>의 인자로 전달해줄 수 있음.
	이 경우, 각 요소를 function의 매개변수로 얻은 return 값을 기준으로 오름차순 정렬됨.

cf. 리스트 요소 삭제방법  del & remove()
	del : 내장 함수. del lst[idx]와 같이 사용. 인덱스를 통해 요소 삭제하고 싶은 경우 사용.
	.remove() : list 제공 함수. lst.remove(val) 값을 통해 요소 삭제하고 싶은 경우 사용.
"""