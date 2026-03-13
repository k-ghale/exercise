

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p == q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


    def __main__():
        p = [1,2]
        q = [1,2]

        print(isSameTree(p,q))
