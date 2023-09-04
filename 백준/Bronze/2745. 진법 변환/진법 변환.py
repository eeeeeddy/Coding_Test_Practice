import sys

answer = 0
N, B = sys.stdin.readline().split()

for i in range(len(N)):
    if ord(N[i]) >= 65:
        answer += ((ord(N[i])-55) * (pow(int(B), len(N)-1-i)))
    else:
        answer += int(N[i]) * (pow(int(B), len(N)-1-i))

print(answer)