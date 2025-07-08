# Iteration
# Time Complexity: O(k * n log k), where k is the number of linked lists and n is the average number of nodes in each list.
# Space Complexity: O(1), since we are not using any additional data structures that grow with input size.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged = None
        for lst in lists:
            merged = self._merge_two_lists(merged, lst)

        return merged

    def _merge_two_lists(self, l1, l2):
        # 1-node dummy head
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        # exactly one of l1 or l2 is non-None here
        tail.next = l1 or l2
        return dummy.next


# Divide And Conquer (Iteration)
# Time Complexity: O(n * log k), where k is the number of linked lists and n is the total number of nodes across k lists.
# Space Complexity: O(1), since we are not using any additional data structures that grow with input size.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        tail.next = l1 or l2

        return dummy.next
