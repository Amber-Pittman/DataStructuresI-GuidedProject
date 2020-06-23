"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import unittest
import sys 
sys.path.append(".../linked_list")
from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
    
    # O(n) when pushing to an array
    # However, we're using LinkedLists! 
    # O(1) because of LL :D
    def push(self, value):
        # add an element to the front of our array
        self.size += 1
        self.storage.add_to_head(value)
    
    # O(n) when popping from an array. 
    # However, we're using LinkedLists! 
    # O(1) because of LL :D
    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.remove_head()
        return node

new_stack = Stack()
print(len(new_stack))
new_stack.push(2)
new_stack.push(3)
new_stack.push(5)
print(len(new_stack))
print(new_stack.storage)
print(f"Removed value is {new_stack.pop()}")

class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_len_returns_0_for_empty_stack(self):
        self.assertEqual(len(self.stack), 0)

    def test_len_returns_correct_length_after_push(self):
        self.assertEqual(len(self.stack), 0)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 1)
        self.stack.push(4)
        self.assertEqual(len(self.stack), 2)
        self.stack.push(6)
        self.stack.push(8)
        self.stack.push(10)
        self.stack.push(12)
        self.stack.push(14)
        self.stack.push(16)
        self.stack.push(18)
        self.assertEqual(len(self.stack), 9)

    def test_empty_pop(self):
        self.assertIsNone(self.stack.pop())
        self.assertEqual(len(self.stack), 0)

    def test_pop_respects_order(self):
        self.stack.push(100)
        self.stack.push(101)
        self.stack.push(105)
        self.assertEqual(self.stack.pop(), 105)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 101)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 100)
        self.assertEqual(len(self.stack), 0)
        self.assertIsNone(self.stack.pop())
        self.assertEqual(len(self.stack), 0)


if __name__ == '__main__':
    unittest.main()