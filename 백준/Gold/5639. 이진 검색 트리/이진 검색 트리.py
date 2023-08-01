import sys
sys.setrecursionlimit(10**6)           # 재귀 제한을 풀어주기 위한 라이브러리 import

class Node:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

class Tree:
   def __init__(self, data):
      self.root = Node(data)
      self.answer = []                 # 후위 순회 결과를 담기 위한 list 변수 생성

   def insert(self, val):              # 전위 순회 결과를 이용해 트리로 만들기 위한 insert 함수
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

   # 왼쪽 > 오른쪽 > 루트
   def postorder(self, node):          # 트리 후위 순회 코드 
      if node.left is not None:
         self.postorder(node.left)
      if node.right is not None:
         self.postorder(node.right)
      self.answer.append(node.val)     # 후위 순회를 진행하면서 answer 리스트에 순회한 값 추가 후 반환
      return self.answer
   
preorder = []                          # 전위 순회 값을 저장하기 위한 빈 리스트 선언

# 입력 코드 (노드 갯수가 정해지지 않았기 때문에 `try...except...`를 이용해야함)
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
tree = Tree(preorder[0])               # 트리의 루트는 무조건 preorder에서 첫 번째 값이므로 그 값을 루트로 가진 트리 생성
for i in range(1, len(preorder)):      # preorder의 인덱스 1부터 수행하면서 트리에 추가
   tree.insert(preorder[i])

result = tree.postorder(tree.root)     # Tree 클래스의 postorder() 함수의 반환 값을 result에 저장

for i in result:
   print(i)
