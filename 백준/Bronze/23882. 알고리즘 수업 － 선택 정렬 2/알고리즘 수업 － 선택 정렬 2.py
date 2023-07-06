n, k = map(int, input().split())

arr = list(map(int, input().split()))
ans = ''

# 교환 횟수를 저장하기위한 변수 생성
cnt = 0 

# index 4부터 1까지 반복문 수행
for i in range(n-1, 0, -1):
    Max = max(arr[:i+1])    # i가 감소하는 반복문을 실행하면서 각각 리스트의 최댓값 탐색
    idx = arr.index(Max)    # 최댓값의 인덱스
    
    if i != idx:
        arr[i], arr[idx] = arr[idx], arr[i]
        cnt += 1            # 교환 횟수 1 증가
    
    if cnt == k:            # 교환 횟수가 k와 같으면 반복문 탈출
        break

if cnt < k:                 # 교환 횟수가 k보다 작을 경우 -1 출력
    print(-1)
else:
    # 제출 형식에 맞게 수정
    for i in range(n-1):
        print(arr[i], end=' ')
    print(arr[-1])