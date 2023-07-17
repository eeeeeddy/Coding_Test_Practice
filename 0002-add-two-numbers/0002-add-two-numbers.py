# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        numLst1, num1 = [], ''
        numLst2, num2 = [], ''
        
        # l1, l2의 값을 head > tail 순서로 numLst에 추가
        while l1 is not None:
            numLst1.append(str(l1.val))
            l1 = l1.next
            
        while l2 is not None:
            numLst2.append(str(l2.val))
            l2 = l2.next
        
        # numLst의 값을 역순으로 전환 후 덧셈 연산을 위해 join하여 형변환
        numLst1.reverse()
        numLst2.reverse()
        
        num1 = int(''.join(numLst1))
        num2 = int(''.join(numLst2))
        
        tmp = str(num1 + num2)

        # 정답 Linked List 구성을 위해 list 및 각 원소를 int로 형변환
        tmp = list(tmp) 
        tmp = [int(i) for i in tmp]
            
        # 정답 Linked List 구성 : head 선언 및 head 앞에 node 추가
        answer = ListNode(tmp[0])
        
        for i in range(1, len(tmp)):
            answer = ListNode(tmp[i], answer)
        
        return answer