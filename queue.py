import unittest
import sys 
sys.path.append(".../linked_list")
from linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 
1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add the new value, to the tail of our list
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        # remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()
        return value



class QueueTests(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_len_returns_0_for_empty_queue(self):
        self.assertEqual(len(self.q), 0)

    def test_len_returns_correct_length_after_enqueue(self):
        self.assertEqual(len(self.q), 0)
        self.q.enqueue(2)
        self.assertEqual(len(self.q), 1)
        self.q.enqueue(4)
        self.assertEqual(len(self.q), 2)
        self.q.enqueue(6)
        self.q.enqueue(8)
        self.q.enqueue(10)
        self.q.enqueue(12)
        self.q.enqueue(14)
        self.q.enqueue(16)
        self.q.enqueue(18)
        self.assertEqual(len(self.q), 9)
    
    def test_empty_dequeue(self):
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(len(self.q), 0)

    def test_dequeue_respects_order(self):
        self.q.enqueue(100)
        self.q.enqueue(101)
        self.q.enqueue(105)
        self.assertEqual(self.q.dequeue(), 100)
        self.assertEqual(len(self.q), 2)
        self.assertEqual(self.q.dequeue(), 101)
        self.assertEqual(len(self.q), 1)
        self.assertEqual(self.q.dequeue(), 105)
        self.assertEqual(len(self.q), 0)
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(len(self.q), 0)

if __name__ == '__main__':
    unittest.main() 