'''

A node is each part of the linked lists. Nodes are the spots in memory. 

The Node class needs a value and a next. 

Describe the initialization behavior for a class: we have to define the init function 
with self and then have self value and self next node. Then we'll want to pass in self, 
value, and next_node. Value and next_node should be optional parameters, so set the 
default to None.

As an example, you can create a node using a variable and then calling Node. You'll pass in 
a value and then the next_node would be a pointer to a new Node. 

We can define a few methods as well within Node. What if we need to get the value from a 
node? Where is the value stored? In self.value. What if we want to be able to change the 
pointers?  In this case, we would do self.next_node equals the new_next that we passed in. 

So far, we can initialize our Node with a value and a next node. We can also get the value
and get next. Additionally, we can set the pointer to a new next.
'''

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node
  
  def set_next(self, new_next):
    self.next_node = new_next

# You can create a Node like this:
#my_node = Node(1, Node())

'''
Our LinkedList is going to be made up of nodes. 

What are the 2 things needed in a linked list? A head and a tail. We're going to initialize
it and assign the head and tail as None. 


'''


class LinkedList:
  def __init__(self):
    self.head = None # Stores a node, that corresponds to our first 
                        # node in the list 
    self.tail = None # stores a node that is the end of the list
  
  def add_to_head(self, value):
    # Artem's version
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # new_node should point to current head
      new_node.next_node = self.head
      # move head to new node
      self.head = new_node

    
  '''
  ADD TO THE TAIL
  What behavior should our linked list be able to do? We definitely need to be able to add 
  to the tail. We'll create a method called add_to_tail. Pass in the value. Now, what if our
  linked list was empty and we try to add to the tail? How will we know if our linked list 
  is empty? Check to see if head is None. 

  So the value that gets passed in, we need to actually make that into a node. We'll create a
  new node and call Node and pass in the value and set the pointer (next node value) to None. 
  We have our Node and we're checking to see if there is no head. If there is no head, what 
  do we need to do? Make the new node the head and also set the tail to new node. 

  ASIDE: Linked lists that have 1 item, the head and the tail are the same.

  If we don't have an empty list, we will always have a tail. Tail is going to be the Node 
  class. We have the set_next method to set our tail on the new_node. Then, we have to set 
  tail to our new node also.

  '''

  def add_to_tail(self, value):
    # create a node to add
    # new_node = Node(value, None)
    # # check if list is empty
    # if self.head is None and self.tail is None:
    #   self.head = new_node
    #   self.tail = new_node
    # else:
    #   # point the node at the current tail, to the new node
    #   self.tail.next_node = new_node
    #   self.tail = new_node

    # # MATT MCCARLEY'S VERSION
    # checking to see if this is equal to None
    new_node = Node(value, None)
    # this is if we have an empty list
    if not self.head:
      self.head = new_node
      self.tail = new_node
    # if we DO have a head in the list
    else:
      self.tail.next_node = new_node
      self.tail = new_node


  '''
  REMOVE THE HEAD
  Why would we want to remove the head of a linked list? Maybe to prepend the list. We need
  a way with our linked list to change the head pointer because the new item in the list
  won't be in the same place as the original head. 

  In this case, like the add_to_tail method, we need to check for an empty head. If it's 
  empty, return None. Then, we need to check if our head has no next value. 
  
  If head has no next (a pointer), there is a single element in the list and we'll return the
  value of head and then we set the head and the tail to None. Setting both to None makes it
  a zero-element Linked List. 

  If the head was not empty AND it more than one item in the linked list, then we go ahead
  and get the value of the head. Once we have the value of the current head, we reset the 
  head to the next node (pointer) and we finally return the value. 

  '''

  # remove the head and return its value
  def remove_head(self):
    # # Artem's version
    # # Is there a head?
    # if not self.head:      
    #   # if list is empty, do nothing
    #   return None
    # # if list only has one element, set head and tail to None
    # if self.head.next_node is None:
    #   head_value = self.head.value
    #   self.head = None
    #   self.tail = None
    #   return head_value
    # # otherwise we have more elements in the list
    # head_value = self.head.value
    # self.head = self.head.next_node
    # return head_value 

    # # MATT MCCARLEY'S VERSION
      # Is there a head?
    if not self.head:
      # if list empty do nothing - return nothing
      return None

    # if head has no next, there is a single element in the LL. 
    if not self.head.get_next():
      # get a reference to the head 
      head = self.head
      # point head and tail to none since there's only one element in the LL
      self.head = None 
      self.tail = None

      return head.get_value()

    # If there is a head and there are TWO OR MORE items in the LL, get the head's value
    value = self.head.get_value()
    # Now we get the value of the current head and reset the head to the next node (pointer)
    self.head = self.head.get_next()
    # And then we return the value
    return value


  '''
  How is it that we have a data structure that only cares if we have a head and a tail?
  Remember that we have the node class that manages everything else. Basically all we need
  is a pointer to the head and the tail. And then these control what's next. 

  '''

  def remove_tail(self):
    if not self.head:
      return None

    if self.head is self.tail:
      value = self.head.get_value()
      self.head = None
      self.tail = None
      return value

    current = self.head

    while current.get_next() is not self.tail:
      current = current.get_next()

    value = self.tail.get_value()
    self.tail = current
    self.tail.set_next(None)
    return value
        

  def contains(self, value):
    # if self.head is None:
    #   return False
    
    # # Artem's Version
    # # Loop through each node, until we see the value, or we cannot go
    # #  further
    # current_node = self.head

    # while current_node is not None:
    #   # check if this is the node we are looking for
    #   if current_node.value == value:
    #     return True

    #   # otherwise, go to the next node
    #   current_node = current_node.next_node
    # return False 


    # MATT MCCARLEY'S VERSION
    if not self.head:
      return False

    # Get a ref to the node we're currently at; update this as we traverse through a LL
    current = self.head
    # Check to see if we're at a valid node
    while current:
      # Return True if the current value we're looking for matches our target value
      if current.get_value() == value:
        return True 

      # update our current node to the current node's next_node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False
  

# example
linked_list = LinkedList()

linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(f'does our LL contain 0? {linked_list.contains(0)}')
print(f'does our LL contain 1? {linked_list.contains(1)}')
print(f'does our LL contain 2? {linked_list.contains(2)}')

linked_list.add_to_head(2)
print(f'The start of the list is {linked_list.head.value}')
linked_list.add_to_head(5)
print(f'The start of the list is {linked_list.head.value}')
linked_list.remove_head()
print(f'The start of the list is {linked_list.head.value}')