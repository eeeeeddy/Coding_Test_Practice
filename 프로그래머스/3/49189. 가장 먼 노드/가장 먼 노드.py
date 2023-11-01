from collections import deque

def solution(n, edge):
    answer = 0
    graph = {}
    distance = {}   # 가장 먼 노드 파악을 위한 딕셔너리 선언
    visited = []    # bfs를 위한 visited 변수
    q = deque()     # bfs를 위한 queue 선언

    for i in range(1, n+2):
        visited.append(False)   # visited 리스트 초기화
        distance[i] = 0         # 1번노드와 각 노드의 거리를 저장하기위한 딕셔너리 생성

    # 무향 그래프 생성
    for i in range(len(edge)):
        v1, v2 = edge[i][0], edge[i][1]
        if v1 not in graph:
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)
        graph[v1].sort()
        if v2 not in graph:
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)
        graph[v2].sort()

    # bfs 수행
    q.append(1)
    visited[1] = True

    while len(q) > 0:   
        v = q.popleft() 

        edge_v = graph[v]   

        for u in edge_v:    
            if not visited[u]:  
                q.append(u)
                visited[u] = True
                distance[u] += distance[v] + 1  # u, v는 인접노드이므로 u의 거리는 v까지의 거리에 1을 더한 것
                                                # v가 1부터 시작하므로 거리는 1부터 증가하게됨

    # 거리 내림차순으로 정렬
    sorted_distance = sorted(distance.items(), key = lambda x : (-x[1]))

    # 거리가 내림차순으로 정렬됬으므로 첫번째 거리 값과 같은 값이 있을 경우 answer += 1
    for i in sorted_distance:
        if i[1] == sorted_distance[0][1]:
            answer += 1

    return answer