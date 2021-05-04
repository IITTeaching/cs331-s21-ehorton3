from unittest import TestCase
import random

class AVLTree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def rotate_right(self):
            n = self.left
            self.val, n.val = n.val, self.val
            self.left, n.left, self.right, n.right = n.left, n.right, n, self.right

        def rotate_left(self):
            ### BEGIN SOLUTION
            n = self.right
            self.val, n.val = n.val, self.val
            self.right, n.right, self.left, n.left = n.right, n.left, n,self.left
            ### END SOLUTION

        @staticmethod
        def height(n):
            if not n:
                return 0
            else:
                return max(1+AVLTree.Node.height(n.left), 1+AVLTree.Node.height(n.right))

    def __init__(self):
        self.size = 0
        self.root = None

    def check_balance(self, t):
        if t.left is None:
            lh = 0
        else:
           lh= height(t.left)
        if t.right is None:
            rh=0
        else:
            rh=height(t.right)
        dif = lh - rh
        if dif >1:
            return "l"
        elif dif <-1:
            return "r"
        else:
            return 0
    @staticmethod
    def rebalance(grand,par,val):
        ### BEGIN SOLUTION
        if grand.left is par:
            if par.left is val:
                grand.rotate_right()
            if par.right is val:
                par.rotate_left()
                grand.rotate_right()
        if grand.right is par:
            if par.left is val:
                par.rotate_right()
                grand.rotate_left()
            if par.right is val:
                grand.rotate_left()
       
        ### END SOLUTION

    def add(self, val):
        assert(val not in self)
        ### BEGIN SOLUTION
        if self.root is None:
            self.root = self.Node(val)
        else:
            nextN = self.root
            valN = None
            moves= []
            while nextN:
                if val>nextN.val:
                    if nextN.right is None:
                        nextN.right = self.Node(val)
                        valN = nextN.right
                        moves.append("r")
                        break
                    else:
                        nextN=nextN.right
                        moves.append("r")
                elif val<nextN.val:
                    if nextN.left is None:
                        nextN.left = self.Node(val)
                        valN = nextN.left
                        moves.append("l")
                        break
                    else:
                        nextN=nextN.left
                        moves.append("l")
            self.add_balance(moves)
        ### END SOLUTION
    
    def add_balance (self,moves):
        # find 3 vals
        findingGrand = True
        a=2
        grand = self.root
        #find first unbalanced parent node (add)
        while findingGrand:
            for i in range (len(moves)-a):
                if moves[i]=="r":
                    grand=grand.right
                else:
                    grand = grand.left
            if grand is self.root:
                findingGrand = False
                break
            else:
                if self.check_balance(grand) is not 0:
                    findingGrand = False
                    break
                else:
                    a+=1
                    grand=self.root
            if a>len(moves):
                findingGrand = False
                break
        b = a-1
        c = a-2
        child = self.root
        grandchild= self.root
        for i in range (len(moves)-b):
                if moves[i]=="r":
                    child=child.right
                else:
                    child = child.left
        for i in range (len(moves)-c):
                if moves[i]=="r":
                    grandchild=grandchild.right
                else:
                    grandchild = grandchild.left
        if grand and child and grandchild:
            if self.check_balance(grand) is not 0:
                self.rebalance(grand,child,grandchild)



    def __delitem__(self, val):
        assert(val in self)
        ### BEGIN SOLUTION
        av2 = AVLTree()
        for i in self:
            if i is not val:
                av2.add(i)
        self.root = av2.root
        ### END SOLUTION
    
    def __contains__(self, val):
        def contains_rec(node):
            if not node:
                return False
            elif val < node.val:
                return contains_rec(node.left)
            elif val > node.val:
                return contains_rec(node.right)
            else:
                return True
        return contains_rec(self.root)

    def __len__(self):
        return self.size

    def __iter__(self):
        def iter_rec(node):
            if node:
                yield from iter_rec(node.left)
                yield node.val
                yield from iter_rec(node.right)
        yield from iter_rec(self.root)

    def pprint(self, width=64):
        """Attempts to pretty-print this tree's contents."""
        height = self.height()
        nodes  = [(self.root, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level < height-1:
                    nodes.extend([(None, level+1), (None, level+1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                if n.left or level < height-1:
                    nodes.append((n.left, level+1))
                if n.right or level < height-1:
                    nodes.append((n.right, level+1))
                repr_str += '{val:^{width}}'.format(val=n.val, width=width//2**level)
        print(repr_str)

    def height(self):
        """Returns the height of the longest branch of the tree."""
        def height_rec(t):
            if not t:
                return 0
            else:
                return max(1+height_rec(t.left), 1+height_rec(t.right))
        return height_rec(self.root)

################################################################################
# TEST CASES
################################################################################
def height(t):
    if not t:
        return 0
    else:
        return max(1+height(t.left), 1+height(t.right))

def traverse(t, fn):
    if t:
        fn(t)
        traverse(t.left, fn)
        traverse(t.right, fn)

# LL-fix (simple) test
# 10 points
def test_ll_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [3, 2, 1]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# RR-fix (simple) test
# 10 points
def test_rr_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [1, 2, 3]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# LR-fix (simple) test
# 10 points
def test_lr_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [3, 1, 2]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# RL-fix (simple) test
# 10 points
def test_rl_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [1, 3, 2]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# ensure key order is maintained after insertions and removals
# 30 points
def test_key_order_after_ops():
    tc = TestCase()
    vals = list(range(0, 100000000, 333333))
    random.shuffle(vals)

    t = AVLTree()
    for x in vals:
        t.add(x)

    for _ in range(len(vals) // 3):
        to_rem = vals.pop(random.randrange(len(vals)))
        del t[to_rem]

    vals.sort()

    for i,val in enumerate(t):
        tc.assertEqual(val, vals[i])

# stress testing
# 30 points
def test_stress_testing():
    tc = TestCase()
    
    def check_balance(t):
        tc.assertLess(abs(height(t.left) - height(t.right)), 2, 'Tree is out of balance')

    t = AVLTree()
   # vals = list(range(1000))
    vals = list(range(200))
    random.shuffle(vals)
    for i in range(len(vals)):
        t.add(vals[i])
        for x in vals[:i+1]:
            tc.assertIn(x, t, 'Element added not in tree')
        traverse(t.root, check_balance)
    random.shuffle(vals)
    for i in range(len(vals)):
        del t[vals[i]]
        for x in vals[i+1:]:
            tc.assertIn(x, t, 'Incorrect element removed from tree')
        for x in vals[:i+1]:
            tc.assertNotIn(x, t, 'Element removed still in tree')
        traverse(t.root, check_balance)



################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_ll_fix_simple,
              test_rr_fix_simple,
              test_lr_fix_simple,
              test_rl_fix_simple,
              test_key_order_after_ops,
              test_stress_testing]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
