def solution(A,B):
    answer = 0

    # A의 가장 작은 수는 B의 가장 큰 수와 곱해서 더해야 최솟값을 구할 수 있음
    A = sorted(A)
    B = sorted(B, reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer