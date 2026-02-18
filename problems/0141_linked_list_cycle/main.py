# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## Solution 1: time O(n), space O(n)
        # visited_nodes = set()
        # curr = head
        # while curr:
        #     if curr in visited_nodes:
        #         return True
        #     else:
        #         visited_nodes.add(curr)
        #         curr = curr.next
        # return False

        ## Solution 2: time O(n), space O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
