import sys
sys.setrecursionlimit(10**6)

class Node:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
         
class Tree:
   def __init__(self, data):
      self.root = Node(data)
      self.answer = []
      
   def insert(self, val):
      node = Node(val)
      curr = self.root
      
      while True:
         if val < curr.val:
            if curr.left is None:
               curr.left = node
               break
            else:
               curr = curr.left
         else:
            if curr.right is None:
               curr.right = node
               break
            else:
               curr = curr.right
               
   def postorder(self, node): # 왼쪽 > 오른쪽 > 루트
      if node.left is not None:
         self.postorder(node.left)
      if node.right is not None:
         self.postorder(node.right)
         
      self.answer.append(node.val)
      return self.answer
      
preorder = []           # 전위 순회 값을 저장하기 위한 빈 리스트 선언

# 입력받기
while True:
   try:
      num = input()
      if num == '':
         break
      else:
         preorder.append(int(num))
   except:
      break

# 트리를 만든 후 후위 순회 구현
tree = Tree(preorder[0])   # 트리의 루트는 무조건 preorder에서 첫 번째 값이므로 루트 생성해줌         

for i in range(1, len(preorder)):
   tree.insert(preorder[i])
   
# print(tree.root.val)             # 50
# print(tree.root.left)            # <__main__.Node object at 0x00000179150DBC50>
# print(tree.root.left.val)        # 30
# print(tree.root.left.left.val)   # 24
# print(tree.root.right.right)     # None

result = tree.postorder(tree.root)

for i in result:
   print(i)
