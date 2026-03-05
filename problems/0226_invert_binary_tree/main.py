# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## Solution 1: iterative BFS - time O(n), space O(n)
        # if not root:
        #     return None
        # queue = [root]
        # while len(queue) > 0:
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         tmp = node.left
        #         node.left = node.right
        #         node.right = tmp
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

        ## Solution 2: DFS - time O(n), space O(n)
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
