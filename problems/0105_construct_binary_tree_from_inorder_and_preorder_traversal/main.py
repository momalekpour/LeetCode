# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # DFS Solution
    # # Time Complexity: recursion stack O(n) and .index function O(n) -> O(n^2)
    # # Space Complexity: O(n) for recursion stack
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if not preorder or not inorder:
    #         return None
    #
    #     root = TreeNode(preorder[0])
    #     mid = inorder.index(root.val)
    #
    #     root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
    #     root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    #
    #     return root

    # DFS + HashMap Solution
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        indices = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
