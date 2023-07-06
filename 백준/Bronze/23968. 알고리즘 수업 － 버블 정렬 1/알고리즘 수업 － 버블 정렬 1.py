import sys

# 시간 초과 해결을 위해 sys.stdin.readline() 사용
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 교환 횟수를 저장하기위한 변수 생성
cnt = 0 

# 인덱스 n-1부터 1까지 반복문 실행
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:   # 리스트에서 앞의 숫자가 더 크면 뒤의 숫자와 swap
            arr[j], arr[j+1] = arr[j+1], arr[j]
            cnt += 1            # 교환 횟수 1 증가
        
            if cnt == k:        # 교환 횟수가 k와 같으면 반복문 탈출
                print(arr[j], arr[j+1])
                break

if cnt < k:                     # 교환 횟수가 k보다 작을 경우 -1 출력
    print(-1)