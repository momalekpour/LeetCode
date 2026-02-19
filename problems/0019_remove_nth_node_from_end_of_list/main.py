# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## Solution 1: naive approach -> time O(n), space O(n)
        # traverse the linklist and store nodes in a array

        ## Solution 2: time O(n), space O(1)
        if not head:
            return None

        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next

        target = l - n
        if target == 0:
            return head.next

        curr = head
        i = 0
        while curr:
            if i + 1 == target:
                if curr.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
                return head
            i += 1
            curr = curr.next
