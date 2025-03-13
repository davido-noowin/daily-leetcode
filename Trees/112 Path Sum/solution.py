class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(node, val):
    if node is None:
        return False
    if node.left is None and node.right is None and val - node.val == 0:
        return True
    else:
        return findTarget(node.left, val - node.val) or findTarget(node.right, val - node.val)