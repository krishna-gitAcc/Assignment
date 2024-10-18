
from typing import List
from collections import deque;


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:

    def createTree(self, input: List):
        if input is None or len(input) == 0:
            return None;

        root = Node(input[0]);
        queue = deque([root]);
        i = 2;

        while i < len(input):
            parent = queue.popleft();

            while i < len(input) and input[i] is not None:
                # print(input[i], " ");
                child = Node(input[i], []);
                parent.children.append(child);
                queue.append(child);
                print(input[i], " ");
                i += 1;

            print("parent: ", parent.val," child count: ", len(parent.children), ": ");
            i += 1;

        return root;

    def postorder(self, root: Node) -> List[int]:
        result = [];
        if root is None:
            return result;

        stack = [(root, False)]
        while len(stack):
            # print("in stack: ", stack, "\n");
            node, visited = stack.pop();
            # print("node: ", node.val, visited, " : ")
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    for child in reversed(node.children):
                        stack.append((child, False))
                        # print(child.val, " ");
        return result


"""
Input: root = [1,null,3,2,4,null,5,6]
"""

solutionObject = Solution()

#-----------------Test Cases:----------------
# input1 =  [1, None, 3, 2, 4, None, 5, 6];

# root1 = solutionObject.createTree(input1);

# print(solutionObject.postorder(root1));


# input2 = input2 = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14];
# root2 = solutionObject.createTree(input2);
# print(solutionObject.postorder(root2));
"""
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
"""

# create a file which file

