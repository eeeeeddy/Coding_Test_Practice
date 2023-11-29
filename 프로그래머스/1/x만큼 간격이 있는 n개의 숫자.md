### x만큼 간격이 있는 n개의 숫자 ###

<hr>

#### 문제 ####
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

#### 제한조건 ####
- x는 -10000000 이상, 10000000 이하인 정수입니다.
- n은 1000 이하인 자연수입니다.

```py

def solution(x, n):
    answer = []
    sum = 0

    for i in range(n):
        sum += x
        answer.append(sum)
    return answer

```

#### 더 나은 풀이 ####

```py

def number_generator(x, n):
    return [i * x + x for i in range(n)]

```