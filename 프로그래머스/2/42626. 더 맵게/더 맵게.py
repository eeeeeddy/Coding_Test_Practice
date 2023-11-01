import heapq

def solution(scoville, K):
    answer = 0
    heap = []   # scoville 저장할 heap 생성
    x = True    # while문 검사 변수 선언
    
    for i in scoville:
        heapq.heappush(heap, i) # heap 생성
    
    while x and len(heap) >= 2:
        if heap[0] >= K:                # heap의 제일 작은 값이 K 이상인지 검사 > 모든 값이 큰 지를 알 수 있음
            return answer              
        else:                           # 작은 값이 있다면 제일 작은 값 두 개를 섞음
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            s = s1 + s2 * 2
            heapq.heappush(heap, s)
            answer += 1
    
    if heap[0] >= K: # scoville의 크기가 2보다 작지만 K보다 클 경우
        return answer
    else:
        return -1    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우