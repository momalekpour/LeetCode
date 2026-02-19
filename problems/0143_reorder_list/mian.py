# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## Solution 1: naive approach - time O(n), space O(n)
        # if not head:
        #     return

        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # l, r = 0, len(nodes) - 1
        # while l < r:
        #     nodes[l].next = nodes[r]
        #     l += 1
        #     if l >= r:
        #         break
        #     nodes[r].next = nodes[l]
        #     r -= 1

        # nodes[l].next = None

        ## Solution 2: time O(n), space O(1)
        # input:    1 2 3 4 5
        # head_one: 1 2 3
        # head_two: 5 4
        # res:      1 5 2 4 3

        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_one = head
        head_two = slow.next
        slow.next = None

        # reverse the second half
        prev, curr = None, head_two
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head_two = prev

        # merge two halves
        curr1, curr2 = head_one, head_two
        while curr1 and curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1 = tmp1
            curr2 = tmp2

        head = head_one
