# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        _map = {}
        
        children = set()
        for r, c, is_left in descriptions:
            if r not in _map:
                root = TreeNode(r)
                _map[r] = root
            else:
                root = _map[r]
            
            if c not in _map:
                child = TreeNode(c)
                _map[c] = child
            else:
                child = _map[c]
            children.add(c)
            
            if is_left:
                root.left = child
            else:
                root.right = child
        
        r = set(_map.keys()) - children
        return _map[ r.pop() ]
                    