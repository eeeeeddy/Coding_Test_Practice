import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n)]  # 미로를 표시할 이중 리스트 생성
q = deque()                     # BFS 탐색을 위한 queue 생성
curr_x, curr_y = 0, 0

for i in range(n):
    s = sys.stdin.readline().strip()
    for j in range(m):
        graph[i].append(int(s[j]))

q.append([curr_x, curr_y]) # 시작 위치 queue에 추가

while q:

    if graph[n-1][m-1] != 1: # 도착지점의 값이 1이 아닐 경우 바로 while문 종료
        print(graph[n-1][m-1])
        break

    curr_x, curr_y = q.popleft()

    # 현재 위치 (curr_x, curr_y)에서 진행할 수 있는 경로 탐색 (미로 범위 내에서, 다음 값이 1인 경우 진행 가능)
    if 0 <= curr_x-1 < n and 0 <= curr_y < m and graph[curr_x-1][curr_y] == 1: # up
        q.append([curr_x-1, curr_y])                        # 다음에 갈 수 있다면 queue에 추가
        graph[curr_x-1][curr_y] = graph[curr_x][curr_y] + 1 # 갈 수 있는 곳이라면 (이전의 값 + 1)로 값을 변경해줌

    if 0 <= curr_x+1 < n and 0 <= curr_y < m and graph[curr_x+1][curr_y] == 1: # down
        q.append([curr_x+1, curr_y])
        graph[curr_x+1][curr_y] = graph[curr_x][curr_y] + 1

    if 0 <= curr_x < n and 0 <= curr_y-1 < m and graph[curr_x][curr_y-1] == 1: # left
        q.append([curr_x, curr_y-1])
        graph[curr_x][curr_y-1] = graph[curr_x][curr_y] + 1

    if 0 <= curr_x < n and 0 <= curr_y+1 < m and graph[curr_x][curr_y+1] == 1: # right
        q.append([curr_x, curr_y+1])
        graph[curr_x][curr_y+1] = graph[curr_x][curr_y] + 1