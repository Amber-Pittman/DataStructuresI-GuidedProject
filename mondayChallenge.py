"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
 appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Input:
[4,3,2,7,8,2,3,1]

Output: 
[2,3]
"""

# a = [4,3,2,7,8,2,3,1]
# array_size = len(a)

# def repeatingInt(a, n):
#   print("Repeating Integers are:")

#   for i in range(0, n):
#     if a[abs(a[i])] >= 0:
#       a[abs(a[i])] = -a[abs(a[i])]
#     else:
#       print(abs(a[i]), end=" ")

# repeatingInt(a, array_size)

array = [4,3,2,7,8,2,3,1]
size = len(array)

for i in range(size):
  array[array[i] % size] = array[array[i] % size] + size

  print("Repeating Integers: ")
  for i in range(size):
    if (array[i] >= size*2):
      print(i, " ")