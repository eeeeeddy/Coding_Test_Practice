# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    val = 0                         # self.val의 값
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def order(node):
            
            if not node:            # 다음 노드가 비어있을 경우 return
                return
            
            order(node.right)       # 오른쪽 자식 노드 > 루트 노드 > 왼쪽 자식 노드 방향으로 순회
    
            self.val += node.val    # 방문한 노드의 값을 변경(val의 누적 합으로 변경해줌)
            node.val = self.val
            
            order(node.left)        # 왼쪽 노드 방문
            
            return node
        
        return order(root)