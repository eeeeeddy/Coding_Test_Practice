"""
# 1. 아이디어
- 이중 for -> W의 갯수, B의 개수 각각 구하기
- BFS 돌면서 위력의 합 갱신

# 2. 시간복잡도
- BFS : O(V+E)
- V : 100 * 100
- E : 4 * 100 * 100
- O(V+E) : 5 * 100 * 100 = 50,000 < 2억 -> 가능

# 3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 여부 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

# 가로, 세로의 크기가 굉장히 헷갈리는 문제! 문제 꼭 잘 읽자!
n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(m)] # 입력 시 개행 문자 삽입을 방지하기 위해 strip() 사용
chk = [[False] * n for _ in range(m)]
W_power, B_power = 0, 0

# 상하좌우의 x좌표, y좌표
# 시작점에서도 위력의 합을 구해야 하기 때문에 검사하기 위해 (0, 0)을 포함
dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]

def bfs(y, x, color):
    result = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()  # queue에서 뽑아낸 좌표에 대해서 상하좌우를 조사하여 1이 있는지 확인
        for k in range(5):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0 <= ny < m and 0 <= nx < n:  # 확인하면서 map을 벗어나는지 검사
                if map[ny][nx] == color and chk[ny][nx] == False:
                    result += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))

    return result ** 2


for j in range(m):
    for i in range(n):
        if map[j][i] == 'W' and chk[j][i] == False:
            chk[j][i] = True
            W_power += bfs(j, i, 'W')
        if map[j][i] == 'B' and chk[j][i] == False:
            chk[j][i] = True
            B_power += bfs(j, i, 'B')

print(W_power, B_power)