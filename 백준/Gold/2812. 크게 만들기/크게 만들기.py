n, k = map(int, input().split())
x = list((map(int, input())))

stack = []  # 정답 생성을 위한 stack 생성
tmp = 0     # 숫자 비교를 위한 임시 변수 생성
idx = k     # 정답 출력을 위한 idx 변수 생성

for i in range(len(x)):
    tmp = x[i]
    
    # 1. 스택이 비어있지 않고,
    # 2. stack[-1] < tmp
    # 3. k != 0 (숫자를 pop() 할 때마다 1씩 감소시킴)
    while stack and stack[-1] < tmp and k != 0:
        stack.pop()
        k -= 1
        if k == 0:  # k가 0일 때 반복문 탈출
            break
            
    # 숫자를 pop()하기 위한 조건 검사 while문이 끝나면 x[i] 추가
    stack.append(x[i])

# (n-k)개 만큼 stack의 앞에서부터 공백없이 출력
for i in stack[0:n-idx]:
    print(i, end='')