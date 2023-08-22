from collections import deque

n, m, v = map(int, input().split())

graph = {}

def init_route_visited(n):  # 방문 체크를 위한 리스트와 경로를 저장하는 리스트 선언 및 초기화 함수
    visited, route = [], []
    
    for i in range(n+1):
        visited.append(False)

    return visited, route

for i in range(m):      # 무향 그래프이기 때문에 두 간선이 모두 연결됨을 표현
    v1, v2 = map(int, input().split())
    if v1 not in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)
    graph[v1].sort()    # 노드 번호 오름차순으로 정렬
    
    if v2 not in graph:
        graph[v2] = [v1]
    else:
        graph[v2].append(v1)
    graph[v2].sort()

def dfs(v, visited):
    route.append(v)
    visited[v] = True   # 방문한 노드는 True로 표시

    edge_v = graph[v]   # 방문한 노드와 연결된 노드중에서 다음 노드로 진행하기 위해 반복문 실행
    for u in edge_v:
        if not visited[u]:  # 연결된 노드가 방문이 안되어있다면 재귀 실행
            dfs(u, visited)

def bfs(v, visited):
    q = deque()

    q.append(v)
    visited[v] = True

    while len(q) > 0:   # q의 길이가 0이 될 때까지 while문 실행
        v = q.popleft() # 이미 방문한 정점일 경우 popleft() -> 그 값을 다음 정점으로 선정

        route.append(v) 
        edge_v = graph[v]   # 이미 방문한 정점의 인접 정점 리스트

        for u in edge_v:    # 반복문을 수행하면서 방문하지 않은 정점을 q에 넣음
            if not visited[u]:  # 방문이 안되어있다면 q에 넣고 visited를 True로 변경
                q.append(u)
                visited[u] = True

    return route

# keyerror 해결 코드 -> 시작 정점 번호가 그래프에 없는 경우 해당 번호만 출력하고 프로그램 종료
if v not in graph.keys():
    print(v)    # dfs의 경우
    print(v)    # bfs의 경우
    exit()

# dfs 경로 출력
visited, route = init_route_visited(n)
dfs(v, visited)
for i in range(len(route)-1):
    print(route[i], end=' ')
print(route[-1])

# bfs 경로 출력
visited, route = init_route_visited(n)
bfs(v, visited)
for i in range(len(route)-1):
    print(route[i], end=' ')
print(route[-1])