# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(r, arr):
            if r == None:
                return
            
            
            traversal(r.left, arr)
            arr.append(r.val)
            traversal(r.right, arr)

        arr = []
        traversal(root, arr)
        return arr
        