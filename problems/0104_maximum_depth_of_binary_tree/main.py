# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## Solutino 1: BFS - time O(n), space O(n)
        # queue = deque()
        # if root:
        #     queue.append(root)
        # depth = 0
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     depth += 1
        # return depth

        ## Solution 2: DFS - time O(n), space O(n)
        if not root:
            return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return 1 + max(l_depth, r_depth)
