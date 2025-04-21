class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestZigZag(root: TreeNode) -> int:
    def maxZigZag(node, left, right):
        if node is None:
            return max(left, right)
        l = maxZigZag(node.left, right + 1, 0)
        r = maxZigZag(node.right, 0, left + 1)
        return max(l, r)

    return maxZigZag(root, 0, 0) - 1
