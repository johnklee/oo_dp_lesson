from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    root = TreeNode(values.pop(0))
    nodes = [root]
    while values and nodes:
        next_nodes = []
        for n in nodes:
            next_value = values.pop(0)
            if next_value:
                n.left = TreeNode(next_value)
                next_nodes.append(n.left)
            next_value = values.pop(0)
            if next_value:
                n.right = TreeNode(next_value)
                next_nodes.append(n.right)
                
            if not values:
                break
                
        nodes = next_nodes
                
    return root