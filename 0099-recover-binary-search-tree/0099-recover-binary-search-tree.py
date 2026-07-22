class Solution:
    def recoverTree(self, root):
        self.x = self.y = self.pred = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.pred and node.val < self.pred.val:
                self.y = node
                if not self.x:
                    self.x = self.pred
                else:
                    return
            self.pred = node
            inorder(node.right)

        inorder(root)
        self.x.val, self.y.val = self.y.val, self.x.val

        