class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q, depth = collections.deque(), 0

        if root:
            q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth