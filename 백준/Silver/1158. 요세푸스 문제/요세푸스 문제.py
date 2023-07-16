#Linked List
#백준 1158
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(value)

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            count += 1
            node = node.next

        return node

    def delete(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index - 1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node

N, K = map(int, input().split())
LL = LinkedList(1)
for i in range (N+1):
    LL.insert(i+2)

ans = []
idx = K - 1
while N:
    idx %= N
    ans.append(LL.delete(idx))
    idx += (K - 1)
    N -= 1

print("<", end="")
for i in range(len(ans)-1):
    print(ans[i], end=", ")
print(ans[len(ans)-1], end="")
print(">")
    