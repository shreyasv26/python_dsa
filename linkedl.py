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

def detectCycle(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
        
    slow = fast = head
    
    # Step 1: Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # Intersection found (Cycle exists)
        if slow == fast:
            start = head
            
            # Step 2: Find the entry point of the cycle
            while start != slow:
                start = start.next
                slow = slow.next
                
            return start
            
    return None

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

class palindrome:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True  # A single node or empty list is always a palindrome

        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.fast.next if hasattr(fast, 'fast') else fast.next.next

        # Step 2: Reverse the second half
        newHead = self.reverseLL(slow)
        temp1, temp2 = head, newHead

        # Step 3: Compare first and second halves
        isPalin = True
        while temp2:  # Only need to check the second half
            if temp1.val != temp2.val:
                isPalin = False
                break
            temp1 = temp1.next
            temp2 = temp2.next

        # Step 4: Restore the list (Optional but highly recommended in interviews)
        self.reverseLL(newHead)

        return isPalin

    # Function to reverse a linked list
    def reverseLL(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

def removeNthFromEnd(head: Node, n: int) -> Node:
    if head is None:
        return None

    count = getCount(head)
    target = count - n

    if target == 0:
        return head.next

    temp = head
    prev = None
    while target > 0:
        prev = temp
        temp = temp.next
        target -= 1

    if prev is not None:
        prev.next = temp.next

    return head

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    slow = head

    # Step 1: Advance fast pointer n steps ahead
    while n > 0:
        fast = fast.next
        n -= 1

    # Edge Case: If fast is None, n equals the length of the list.
    # This means we need to remove the head node.
    if fast is None:
        return head.next

    # Step 2: Move both until fast reaches the last node
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Step 3: Delete the target node
    slow.next = slow.next.next

    return head

def segregateEvenOdd(self, head):
        # Edge case: If list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Create pointers for the heads and tails of even and odd lists
        evenHead = evenTail = None
        oddHead = oddTail = None

        # Pointer to traverse the list
        current = head

        # Traverse the linked list
        while current:

            # If the current node has even value
            if current.data % 2 == 0:
                if not evenHead:
                    evenHead = evenTail = current
                else:
                    evenTail.next = current
                    evenTail = current

            else:
                # If the current node has odd value
                if not oddHead:
                    oddHead = oddTail = current
                else:
                    oddTail.next = current
                    oddTail = current

            # Move to next node
            current = current.next

        # If no even nodes found, return odd list
        if not evenHead:
            return oddHead

        # If no odd nodes found, return even list
        if not oddHead:
            return evenHead

        # Combine even and odd lists
        evenTail.next = oddHead

        # Set end of list to null
        oddTail.next = None

        return evenHead

def deleteMiddle(head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
            
        slow = head
        fast = head
        prev = None
        
        # Fast & Slow pointer approach to find the middle
        while fast and fast.next:
            prev = slow              
            slow = slow.next
            fast = fast.next.next
            
        # Skip the middle node
        prev.next = slow.next

        return head

class sortList:
    def getMid(self, head: ListNode) -> ListNode:
        s = head
        f = head
        prev = None
        while f is not None and f.next is not None:
            prev = s
            s = s.next
            f = f.next.next
        if prev is not None:
            prev.next = None
        return s

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummyhead = ListNode(0)
        temp = dummyhead

        while left is not None and right is not None:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left if left is not None else right
        return dummyhead.next

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        left = sortList(head)
        right = sortList(mid)
        return self.merge(left, right)

def intersectionPresent(head1, head2):
    d1, d2 = head1, head2
    # Traverse both lists, when one reaches the end, redirect it to the head of the other list
    while d1 != d2:
        d1 = head2 if d1 is None else d1.next
        d2 = head1 if d2 is None else d2.next

    return d1  # If they meet, return the intersection node, otherwise None

