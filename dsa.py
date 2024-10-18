
from typing import List
from collections import deque;


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:

    def createTree(input: List):
        if input == None or input.size() == 0:
            return None;

        root = Node(input[0]);
        queue = deque([root]);
        i = 2;

        while i < len(input):
            parent = queue.popleft();

            while i< len(input) and input[i] is not None:
                child = Node(input[i]);
                parent.children.append(child);
                queue.append(child);
                i += 1;
            i += 1;

        return root;

    def postorder(self, root: Node) -> List[int]:
        pass


"""
Input: root = [1,null,3,2,4,null,5,6]
"""

"""
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
"""

# create a file which file

