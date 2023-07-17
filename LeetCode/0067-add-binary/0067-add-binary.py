class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # 문자열 2진수를 10진수로 변환
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # num1과 num2를 더한 후 2진수로 변환
        sum = str(bin(num1+num2)[2:])
        
        return sum

        