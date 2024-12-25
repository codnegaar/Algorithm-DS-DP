'''

Leetcode BFS 515 Find the Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each tree row (0-indexed).

Example 1:
        Input: root = [1,3,2,5,3,null,9]
        Output: [1,3,9]

Example 2:
        Input: root = [1,2,3]
        Output: [1,3]
 
Constraints:
        The number of nodes in the tree will be in the range [0, 104].
        -231 <= Node.val <= 231 - 1

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root: Optional[TreeNode], depth: int) -> None:
      if not root:
        return
      if depth + 1 > len(ans):
        ans.append(root.val)
      else:
        ans[depth] = max(ans[depth], root.val)

      dfs(root.left, depth + 1)
      dfs(root.right, depth + 1)

    dfs(root, 0)
    return ans

# Second solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            max_level = q[0].val
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                max_level =max(max_level, node.val)

                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_level)
        return res




        

