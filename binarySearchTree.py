"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:

1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.

2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert
        if value < self.value:
            # if new value < self.value
                # IF self.left is already taken by a node
                    # make that (left) node, call insert 
                # set the left to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        if value >= self.value:
            # if new value >= self.value
                # IF self.right is already taken by a node
                    # make that (right) node call insert 
                # set the right child to the new node with new value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value > target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value < target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        if self.right is None:
            return self.value
        
        max = self.right.get_max()
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        # if you can go right, call for_each on the right tree
        if self.left:
            self.left.for_each(fn)
        
        fn(self.value)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# root_node = BSTNode(8)
# root_node.insert(3)
# root_node.insert(4)
# root_node.insert(2)
# root_node.insert(10)
# root_node.insert(9)
# root_node.insert(12)

# # const print_node = (x) => { console.log(x) }
# print_node = lambda x: print(f'current_node is : {x}')

# root_node.for_each(print_node)

import unittest
import random
import sys
import io

class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BSTNode(5)

    def test_insert(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(6)
        self.assertEqual(self.bst.left.right.value, 3)
        self.assertEqual(self.bst.right.left.value, 6)
        
    def test_handle_dupe_insert(self):
        self.bst2 = BSTNode(1)
        self.bst2.insert(1)
        self.assertEqual(self.bst2.right.value, 1)

    def test_contains(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertTrue(self.bst.contains(7))
        self.assertFalse(self.bst.contains(8))

    def test_get_max(self):
        self.assertEqual(self.bst.get_max(), 5)
        self.bst.insert(30)
        self.assertEqual(self.bst.get_max(), 30)
        self.bst.insert(300)
        self.bst.insert(3)
        self.assertEqual(self.bst.get_max(), 300)

    def test_for_each(self):
        arr = []
        cb = lambda x: arr.append(x)

        v1 = random.randint(1, 101)
        v2 = random.randint(1, 101)
        v3 = random.randint(1, 101)
        v4 = random.randint(1, 101)
        v5 = random.randint(1, 101)

        self.bst.insert(v1)
        self.bst.insert(v2)
        self.bst.insert(v3)
        self.bst.insert(v4)
        self.bst.insert(v5)

        self.bst.for_each(cb)

        self.assertTrue(5 in arr)
        self.assertTrue(v1 in arr)
        self.assertTrue(v2 in arr)
        self.assertTrue(v3 in arr)
        self.assertTrue(v4 in arr)
        self.assertTrue(v5 in arr)

    # def test_print_traversals(self):
    #     # WARNING:  Tests are for Print()
    #     # Debug calls to Print() in functions will cause failure

    #     stdout_ = sys.stdout  # Keep previous value
    #     sys.stdout = io.StringIO()

    #     self.bst = BSTNode(1)
    #     self.bst.insert(8)
    #     self.bst.insert(5)
    #     self.bst.insert(7)
    #     self.bst.insert(6)
    #     self.bst.insert(3)
    #     self.bst.insert(4)
    #     self.bst.insert(2)

    #     self.bst.in_order_print(self.bst)

    #     output = sys.stdout.getvalue()
    #     self.assertEqual(output, "1\n2\n3\n4\n5\n6\n7\n8\n")

    #     sys.stdout = io.StringIO()
    #     self.bst.bft_print(self.bst)
    #     output = sys.stdout.getvalue()
    #     self.assertTrue(output == "1\n8\n5\n3\n7\n2\n4\n6\n" or
    #                     output == "1\n8\n5\n7\n3\n6\n4\n2\n")

    #     sys.stdout = io.StringIO()
    #     self.bst.dft_print(self.bst)
    #     output = sys.stdout.getvalue()
    #     self.assertTrue(output == "1\n8\n5\n7\n6\n3\n4\n2\n" or
    #                     output == "1\n8\n5\n3\n2\n4\n7\n6\n")

    #     sys.stdout = io.StringIO()
    #     self.bst.pre_order_dft(self.bst)
    #     output = sys.stdout.getvalue()
    #     self.assertEqual(output, "1\n8\n5\n3\n2\n4\n7\n6\n")

    #     sys.stdout = io.StringIO()
    #     self.bst.post_order_dft(self.bst)
    #     output = sys.stdout.getvalue()
    #     self.assertEqual(output, "2\n4\n3\n6\n7\n5\n8\n1\n")

    #     sys.stdout = stdout_  # Restore stdout

if __name__ == '__main__':
    unittest.main()