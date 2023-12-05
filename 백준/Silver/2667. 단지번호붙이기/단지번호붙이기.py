"""
1. 아이디어
- 2중 for문을 수행하면서 값이 1이고, 방문하지 않았다면 DFS 실행
- DFS를 통해 찾은 값을 저장 후 정렬해서 출력

2. 시간복잡도
- DFS : O(V+E)
- V : N^2
- E : 4 * N^2
- V+E : 5 * N^2 ~= N^2 ~= 625 <= 2억 => 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문 여부 : bool[][]
- 결과값 : int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(y, x):
    global each # 전역변수 each를 사용하기 위해 선언
    each += 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<= ny < N and 0<= nx < N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True

            # DFS로 크기 구하기
            each = 0
            dfs(j, i)

            # 크기를 결과 리스트에 넣기
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)