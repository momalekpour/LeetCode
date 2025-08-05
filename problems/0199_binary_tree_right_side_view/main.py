# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS Solution
    # Time and Space Complexity: O(n)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            is_first_node = True
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    if is_first_node:
                        res.append(node.val)
                        is_first_node = False
                    queue.append(node.right)
                    queue.append(node.left)

        return res
