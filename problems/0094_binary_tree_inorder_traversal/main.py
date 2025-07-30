# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Rucrsive Solution (DFS)
    ## time complexity: O(n)
    ## sapce complexity: O(h + n), h for the call stack and n for the output array
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root_node):
            if not root_node:
                return
            inorder(root_node.left)
            res.append(root_node.val)
            inorder(root_node.right)

        inorder(root)
        return res
