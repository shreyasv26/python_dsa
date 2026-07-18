# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# for null in java use None here

def deleteNode(self, node) -> None:
    if node.val==None or node.next==None:
        return 
    
    node.val=node.next.val
    node.next=node.next.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.bottom = None

class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

def display(head: Node) -> None:
    if head is None:
        print("NULL")
    else:
        temp = head
        while temp.next is not None:
            print(f"{temp.data}-> ", end="")
            temp = temp.next
        print("null")

def constructLL(arr: list[int]) -> Node:
    if not arr:
        return None
    dummy = Node(arr[0])
    temp = dummy
    for i in range(1, len(arr)):
        newnode = Node(arr[i])
        dummy.next = newnode
        dummy = dummy.next
    return temp

def insertAtEnd(head: Node, x: int) -> Node:
    newnode = Node(x)
    newnode.next = None
    if head is None:
        head = newnode
        return newnode
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
    return head

def getCount(head: Node) -> int:
    count = 0
    temp = head
    if head is None:
        return 0
    else:
        while temp is not None:
            count += 1
            temp = temp.next
    return count

def searchKey(n: int, head: Node, key: int) -> bool:
    if head is None:
        return False
    else:
        temp = head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
    return False

def constructDLL(arr: list[int]) -> Node:
    if not arr:
        return None
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        newnode = Node(arr[i])
        temp.next = newnode
        newnode.prev = temp
        temp = temp.next
    return head

def addNode(head: Node, p: int, x: int) -> Node:
    count = 0
    newnode = Node(x)
    if head is None and p == 0:
        return newnode
    elif head is None and p > 0:
        return head
    else:
        temp = head
        while temp is not None and count != p:
            temp = temp.next
            count += 1
        if count != p or temp is None:
            return head
        if temp.next is None:
            newnode.next = None
            newnode.prev = temp
            temp.next = newnode
        else:
            newnode.next = temp.next
            temp.next.prev = newnode
            temp.next = newnode
            newnode.prev = temp
    return head

def deleteNode(head: Node, x: int) -> Node:
    if head is None or x <= 0:
        return head

    temp = head

    if x == 1:
        head = head.next
        if head is not None:
            head.prev = None
        return head

    count = 1
    while temp is not None and count < x:
        temp = temp.next
        count += 1

    if temp is None:
        return head

    if temp.prev is not None:
        temp.prev.next = temp.next
    if temp.next is not None:
        temp.next.prev = temp.prev

    return head

def reverseDLL(head: DLLNode) -> DLLNode:
    current = head
    prev = None
    next_node = None
    while current is not None:
        next_node = current.next
        current.next = prev
        if prev is not None:
            prev.prev = current
        current.prev = next_node
        prev = current
        current = next_node
    return prev

def reverseLL(head: Node) -> Node:
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverseLLRecursion(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    newHead = reverseLLRecursion(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newHead

def lengthCycle(head: Node) -> int:
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            temp = slow
            length = 1
            while temp.next != slow:
                temp = temp.next
                length += 1
            return length
    return 0

def isPalindrome(head: Node) -> bool:
    if head is None or head.next is None:
        return True
        
    s = head
    f = head

    while f is not None and f.next is not None:
        s = s.next
        f = f.next.next
        
    newhead = reverseLLRecursion(s)
    newtemp = newhead
    temp = head
    
    while newtemp.next is not None:
        if temp.data != newtemp.data:
            return False
        temp = temp.next
        newtemp = newtemp.next

    reverseLLRecursion(newhead)
    return True

