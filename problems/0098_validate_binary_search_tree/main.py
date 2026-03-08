# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ## Solution 1: brute force - time O(n^2), space O(n)
        ## Solution 2: dfs - time O(n), space O(n)
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and
                    node.val < right):
                return False
            l = valid(node.left, left, node.val)
            r = valid(node.right, node.val, right)
            return l and r

        return valid(root, float("-inf"), float("inf"))
