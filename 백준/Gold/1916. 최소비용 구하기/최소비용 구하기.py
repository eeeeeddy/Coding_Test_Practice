import heapq, sys

n = int(sys.stdin.readline()) # 시간초과를 해결하기위해 sys.stdin.readline() 사용
m = int(sys.stdin.readline())

graph = {}

for i in range(m):
    bstart, bend, fee = map(int, sys.stdin.readline().split())
    if bstart not in graph:
        graph[bstart] = {bend:fee}
    else:
        if bend in graph[bstart] and graph[bstart][bend] <= fee: # 같은 경로임에도 비용이 저렴한 경우가 입력이 들어올 경우 처리하기 위한 조건문
            graph[bstart].update({bend:graph[bstart][bend]})
        else:
            graph[bstart].update({bend:fee})

start, end = map(int, sys.stdin.readline().split())

distances = [ float('inf') for i in range(n+1) ] # 도시 번호 그대로 인덱스 접근을 위해 하나 크게 테이블 생성

# 우선순위 큐를 활용한 다익스트라 알고리즘 풀이
distances[start] = 0 # 시작 지점의 거리는 0
queue = []
heapq.heappush(queue, [distances[start], start]) # queue에 시작노드의 거리와 시작노드 번호 추가

while queue: # queue에 남아있는 노드가 없으면 종료
    current_distance, current_destination = heapq.heappop(queue) # 탐색할 노드의 거리, 탐색할 노드 번호를 queue에서 가져옴

    if distances[current_destination] < current_distance: # 기존의 거리보다 길다면 다음 루프 진행
        continue
    
    if current_destination in graph:
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance # 해당 노드를 거쳐갈 때의 거리
            if distance < distances[new_destination]: # 테이블의 거리보다 작다면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination]) # 다음 인접 거리 계산을 위해 queue에 추가

print(distances[end]) # 문제에서 주어진 도착 지점의 최단 거리 출력