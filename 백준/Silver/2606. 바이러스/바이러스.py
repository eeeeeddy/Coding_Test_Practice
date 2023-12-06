"""
1. 아이디어
- 네트워크 구성 후 while문을 수행하면서 BFS 진행

2. 시간복잡도 : O(V+E)
- V : N
- E : 4*N
- O(V+E) : 5*N = 500 < 2억 => 가능

3. 자료구조
- 네트워크를 구성할 2차원 배열 : int[][]
- 방문 여부 2차원 배열 : bool[][]
- BFS : Queue
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
chk = [False for _ in range(n+1)]
result = 0
q = [1] # 1번 컴퓨터가 감염되었기 때문에 queue에 1 삽입
chk[1] = True # 1번 컴퓨터가 감염되었기 때문에 queue에 1 삽입

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]  # a에 b 연결
    graph[b] += [a]  # b에 a 연결 -> 양방향

# BFS
while q:
    ex = q.pop()
    for nx in graph[ex]:
        if chk[nx] == False:
            chk[nx] = True # 방문 체크 표시
            q.append(nx)
            result += 1 # 감염된 총 컴퓨터 수

print(result)