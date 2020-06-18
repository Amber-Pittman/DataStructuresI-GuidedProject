count = 0

def my_print_counter(thing_to_print):
  global count
  count += 1
  print(thing_to_print)

#my_items = [1,2,3,4,5,6,7,8,9,10]


"""
O(1) - Constant Time

The input - no matter how big it gets - the number of operations 
stay the same.

The line will be flat.
"""

# def print_first_item(items):
#   my_print_counter(items[0])

# print_first_item(my_items)

"""
O(n) - Linear Time

The input is a collection of items then it loops through each item 
in the collection. And then it will print that out. 

The line will be diagonal.
"""

# def print_all_items(items):
#   for item in items:
#     my_print_counter(item)

# print_all_items(my_items)

"""
O(n^2) - Quadratic Time

When the input gets passed in, we have an outer loop and an inner
loop. Then, each time we print a Tuple for the first item and the 
second item. 

In the case of the code below, when run, it prints out:
First Loop goes through and gets both the 1st item and the 2nd item.
Because there are 10 items in my_list, the 1st item has to loop 10 
times in order to get all of the 10 items in the 2nd items.

It will have to loop 10 times to get all the items required.

On a graph the line will slightly go up at first and then abruptly
shoots up the graph. 

Quadratic Time is LESS EFFICIENT than Linear Time.

First Loop
(1, 1)
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(1, 6)
(1, 7)
(1, 8)
(1, 9)
(1, 10)
Second Loop
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(2, 5)
(2, 6)
(2, 7)
(2, 8)
(2, 9)
(2, 10)
Third Loop
(3, 1)
(3, 2)
(3, 3)
(3, 4)
(3, 5)
(3, 6)
(3, 7)
(3, 8)
(3, 9)
(3, 10)
Fourth Loop
(4, 1)
(4, 2)
(4, 3)
(4, 4)
(4, 5)
(4, 6)
(4, 7)
(4, 8)
(4, 9)
(4, 10)
Fifth Loop
(5, 1)
(5, 2)
(5, 3)
(5, 4)
(5, 5)
(5, 6)
(5, 7)
(5, 8)
(5, 9)
(5, 10)
Sixth Loop
(6, 1)
(6, 2)
(6, 3)
(6, 4)
(6, 5)
(6, 6)
(6, 7)
(6, 8)
(6, 9)
(6, 10)
Seventh Loop
(7, 1)
(7, 2)
(7, 3)
(7, 4)
(7, 5)
(7, 6)
(7, 7)
(7, 8)
(7, 9)
(7, 10)
Eight Loop
(8, 1)
(8, 2)
(8, 3)
(8, 4)
(8, 5)
(8, 6)
(8, 7)
(8, 8)
(8, 9)
(8, 10)
Ninth Loop
(9, 1)
(9, 2)
(9, 3)
(9, 4)
(9, 5)
(9, 6)
(9, 7)
(9, 8)
(9, 9)
(9, 10)
Tenth Loop
(10, 1)
(10, 2)
(10, 3)
(10, 4)
(10, 5)
(10, 6)
(10, 7)
(10, 8)
(10, 9)
(10, 10)
"""

# def print_all_possible_ordered_pairs(items):
#   for first_item in items:
#     for second_item in items:
#       my_print_counter((first_item, second_item))

# print_all_possible_ordered_pairs(my_items)

"""
N could be the actual input, or the size of the input.

The first example below will be linear - O(n) - because the number
of operations we have - the number of times we print - will be 
linear to the size of the input. In this particular case, we are not
passing in a list or a collection. It's an actual number. 

Sometimes it's a list or collection. Other times, it's a number. 
We can still use Big O notation to describe them.
"""

# def say_hi_n_times(n):
#   for time in range(n):
#     my_print_counter("hi")

# say_hi_n_times(10)


# def print_all_items(items):
#   for item in items:
#     my_print_counter(item)

# print_all_items(my_items)

"""
Drop the constants

O(2n) is simplified to what?
Here we don't have nested for loops. Instead we have 2 different 
for loops. 

How would we describe this in Big O Notation? O(2n) because 
my_items is still 5 items - 1 through 5. 

We'll go through each of those items and print. If you run it, it
will return the first loop's 5 numbers, the the 2nd loop's
5 numbers, and then it's done. In the terminal, it looks like this:

  1
  2
  3
  4
  5
  1
  2
  3
  4
  5

This is where Big O Notation is really nice. Even though if we 
look on a graph, 2n is less efficient than O(n) even though they are
both Linear. So we could just simplify this to O(n). 

That being said, even though the code below is described as O(n)
just like if it only had 1 for loop, with both loops, it doubles the
time. 

We always simplify by dropping the constants, but that doesn't mean
that constants don't matter sometimes. 
"""

new_items = [1,2,3,4,5]

# O(2n) is simplified to what? O(n)
# def print_all_items_twice(items):
#   for item in items:
#     my_print_counter(item)

#   # Once more, with feeling:
#   for item in items:
#     my_print_counter(item)

# print_all_items_twice(new_items)

'''
0(1 + n/2 + 100) is simplified to what? 

When we pass in the input (items) and run the counter, we can describe it as
0(1) because no matter how big items is, we only print one item. 

We start our index at zero and we go up to halfway through the size of the index 
item (middle_index) and each time we print something out. We would describe this
as O(n/2).

When going through the range, we would describe this as O(100) because we're not
simplifying yet. No matter how bit items is, we're going to print "hi" 100 times. 

So all of these together we would write like 0(1 + n/2 + 100). How would we 
simplify this? In this case, we drop the constants and we also drop the less
significant terms. Therefore, we would simplify this whole thing as O(n). 
'''

# def print_first_item_then_first_half_then_say_hi_100_times(items):
#   my_print_counter(items[0]) # O(1)

#   middle_index = len(items) / 2 # O(n/2)
#   index = 0

#   while index < middle_index:
#     my_print_counter(items[index])
#     index += 1

#   for time in range(100): # O(100)
#     my_print_counter("hi")

#   print_first_item_then_first_half_then_say_hi_100_times(new_items)

"""
Drop the less significant terms. 

O(n + n^2) is simplified to what?

Run through every number in numbers with a for loop; this is O(n). 

Then, we start into another for loop except it's a nested for loop. Nested for
loops are Quadratic, meaning that it is O(n^2) - O of n squared.

Which one of these for loops controls the shape of the function more? The 2nd one, 
making it O(n^2). On a graph, the shape of O(n) an O(n^2) is the same - it just 
shifted to the right a bit.

O(n^2) IS REALLY INEFFICIENT! 
"""

# def print_all_nums_then_all_pair_sums(numbers):
#   print("These are the numbers:")
#   for num in numbers: # O(n)
#     my_print_counter(num)

#   print("and these are their sums:")
#   for first_num in numbers: # O(n^2)
#     for second_num in numbers:
#       my_print_counter(first_num + second_num)

# print_all_nums_then_all_pair_sums(new_items)


"""
We are usually talking about the "worst case" when we're talking about Big O. Why
does that matter?

How many operations will run we call contains? How many times will it have to go
through the for loop before it returns? 10 in the worst case. 

What would the needle that's passed in the function call as 1 need to be in order
for it to run 10 times. In some cases you could get lucky and the very first thing
you're looking for is found and it only took one operation. BUT worst case is that
it has to go through the entire array. The worst case would be Linear. 
"""

my_haystack = [1,2,3,4,5,6,7,8,9,10]

def contains(haystack, needle):
  #does the haystack contain the needle?
  for item in haystack:
    if item == needle:
      return True

  return False

contains(my_haystack, 1) 
  # If you insert 10 where the 1 is, it will have to go through the loop 10 times.



"""
Things to remember with Big O:
1. Sometimes constants matter (even though we can drop them in Big O)
2. Beware of premature optimization.


You can use the graphing calculator at www.desmos.com/calculator

"""