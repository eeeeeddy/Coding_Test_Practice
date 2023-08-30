n = int(input())
s = input()
answer = 0

# ord() : 문자를 아스키 코드값으로 변환해주는 파이썬 내장함수
for i in range(len(s)):
    answer += (ord(s[i]) - 96) * pow(31, i)

print(answer)