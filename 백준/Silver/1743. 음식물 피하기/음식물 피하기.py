"""
1. 아이디어
- 입력받은 graph의 크기와 음식물의 좌표를 가지고 graph 구성
- 이중 for문을 통해 dfs 수행
- 인접한 음식물의 크기를 구한 후 max 구하기

2. 시간복잡도
- O(V+E)
- V : N*M
- E : 4*N*M
- O(V+E) : 5*N*M = 5*100*100 = 50,000 < 2억 => 가능

3. 자료구조
- 그래프를 저장할 2차원 배열 : int[][]
- 방문 여부를 저장할 2차원 배열 : bool[][]
"""

import sys
sys.setrecursionlimit(10**6) # 최대 재귀 깊이 변경
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
chk = [[False] * m for _ in range(n)]
each, result = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# graph 구성
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

def dfs(y, x):
    global each # 전역변수 each를 사용하기 위해 선언
    each += 1

    for l in range(4):
        ny = y + dy[l]
        nx = x + dx[l]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and chk[i][j] == False:
            # 방문 체크 표시
            chk[i][j] = True

            # dfs를 수행하면서 음식물의 크기 측정
            each = 0
            dfs(i, j)

            # 음식물의 크기 갱신 (최대)
            result =  max(result, each)

print(result)