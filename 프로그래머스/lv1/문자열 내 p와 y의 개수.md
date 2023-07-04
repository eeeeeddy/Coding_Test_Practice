### 문자열 내 p와 y의 개수 ###

<hr>

#### 문제 ####
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

#### 제한조건 ####
- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

```py

def solution(s):
    answer = True
    p, y = 0, 0

    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
        
    if p == y or p == y == 0:
        return True
    else:
        return False

```

#### 더 나은 풀이 ####
lower()와 count()의 사용으로 간결한 코딩이 가능하다.

```py

def numPY(s):

    return s.lower().count('p') == s.lower().count('y')


```