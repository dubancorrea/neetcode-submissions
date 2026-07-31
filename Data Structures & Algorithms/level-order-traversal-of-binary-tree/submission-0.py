# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []  # it holds a sublist per level
        if not root:
            return result

        queue = deque([root]) # queue starting with just the root node

        while queue:   # this keep going until there are not nodes left
            level_size = len(queue)  # number of nodes currently in this level
            level_values = [] #values collected

            for i in range(level_size):  # process the nodes belonging to this level
                node = queue.popleft()
                level_values.append(node.val) # record its value for this level

                if node.left:
                    queue.append(node.left) # if there is a left child add it to the queue in the next level
                
                if node.right:
                    queue.append(node.right)

            result.append(level_values)
        return result
        




        
