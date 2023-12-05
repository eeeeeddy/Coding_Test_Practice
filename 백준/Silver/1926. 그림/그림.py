"""
1. 아이디어
- 이중 for -> 값 1 && 방문 X -> BFS
- BFS 돌면서 그림 개수+1, 최대값 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250,000 = 약 1,000,000 < 2억 -> 가능!

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 여부 : bool[][]
- Queue(BFS)
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
cnt, maxv = 0, 0  # 전체 그림 개수, 그림의 크기의 최대값

# 상하좌우의 x좌표, y좌표
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    result = 1  # 그림(1이 연속된 부분)의 크기를 저장하기 위한 변수
    q = [(y, x)]
    while q:
        ey, ex = q.pop()  # queue에서 뽑아낸 좌표에 대해서 상하좌우를 조사하여 1이 있는지 확인
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0 <= ny < n and 0 <= nx < m:  # 확인하면서 map을 벗어나는지 검사
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    result += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))

    return result

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True  # 방문 표시
            cnt += 1  # 전체 그림 개수 += 1
            maxv = max(maxv, bfs(j, i))  # BFS를 통해서 그림의 크기를 구하고, 최대값 갱신

print(cnt)
print(maxv)