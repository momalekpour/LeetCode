class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        # initialize head and tail with dummy nodes for easier insertion and deletion
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr and curr != self.tail:
            if i == index:
                return curr.val
            else:
                curr = curr.next
                i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, prev=self.head, next=self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                new_node = ListNode(val, prev=curr.prev, next=curr)
                curr.prev.next = new_node
                curr.prev = new_node
                break
            else:
                curr = curr.next
                i += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0
        while curr and curr != self.tail:
            if i == index:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                break
            else:
                curr = curr.next
                i += 1
