import math 
from math import sqrt


'''
When we want to figure out how this function grows, we want to ask if this function 
will do more things if we put a larger value in. 

'''

'''
Constant time == O(1) (or O(c) )

You can also say O(c) to indicate there's a constant that we didn't
  choose to figure out

If you have a constant value, you don't have to add each runtime up. It will be a 
  constant automatically.

It stays O(1) not because it's only going to do 1 thing. It just means that 
  it's not going to grow at all. 

We don't care if it does 4 steps or if it does 1 step. 

Looking at the graph, Contant Time falls into the green range. 
'''

def mult_2(n): # O(1) + O(1) + O(1) + O(1) = O(4) => O(1)
  print(n) # O(1)
  if n == 5: # O(1)
    print("hooray") # O(1)
  return n * 2  # O(1) 
  # The 2 in the return is a constant value because it has nothing to do with n.


'''
Linear time == O(n)

Linear time is a 1:1 growth at a steady pace

Loops run several steps so we need to think about that a little bit differently.

'''

def foo(n): # O(n)
  for i in range(0, n): # O(n) * O(1) [from the lines below]  => O(n)
    # the total runtime of the code in the loop is O(1)
    print(i) # O(1)
    print(i) # O(1)
    # The sum of everything inside the loop is O(1) + O(1) = O(2) => Reduce to O(1)
    # Then, we want to multiply the sum by the number of times the for loop runs in relation
    #   to n.
    # With the range starting at zero, and then you make n 10, it will loop 10x. It will
    #   run in relation to n. It's no longer just a number - it's related to n. We can't just
    #   say it run 10 times if there's a billion. So we have to specify that it runs in terms
    #   of n.

'''
Quadratic time (Polynomial Time) == O(n^2)

Slower than Linear. It gets huge really fast. 

The s line + Loops  + return > take worst runtime and simplify to that
'''

def bar(n):  # O(1) + O(n^2) + O(1) ==> O(n^2) 
  s = 0 # O(1)
  # Loop 1 * Loop 2 = n squared
  # O(n) * O(n) = O(n^2)
  for i in range(0, n): # O(n) # there's no constant. Runs in relation to n so O(n)
    for j in range(0, n): # O(n) * O(1) = O(n) this loop runs in linear time
      s += i * j # O( 1 )
  
  return s # O(1)

'''
This version doesn't have a name; it's still polynomial; n to the any number that is NOT 1

O(n) * O( sqrt(n) ) == O(n * sqrt n) === O(n ^ 1.5)

This is also a variant of O(n) * log(n)

Although there's a 2nd loop, it's drastically quicker b/c of sq root
'''

def baz(n):
  s = 0

  for i in range(n): # O(n)
    for j in range(int(sqrt(n))): # O(sqrt(n)) ||  O(n^0.5)
      s += i * j # O(1)
  
  return s


'''
Sublinear Time == Logarithmic Time

Sublinear is when the input is halved (or another division) every step of the loop

Logarithmic is better than Linear Time

Think logarithmic! 

log(n)
'''

def divider(n):
  # determine how many times it will loop
    # if n = 8 the number of steps; first it will 8/2 = 4 then run again  until it hits 0
    # Num of steps: 3x
  while n >= 1: # O( log(n)) 
    print(n) # O(1)
    n = n // 2 # O(1)

    # n = 8 => 3 steps
    # n = 16 => 4 steps
    # n = 32 => 5 steps

    # If there is division in the loop, you can assume it's going to be log(n)