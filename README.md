# DataStructuresI-GuidedProject

### Time Complexity

You can have different algos that give the same result but just take different time to get there. This is why it's important to learn about efficiency because clearly, if there's a solution that takes 0.02 ms to sort vs 0.6 ms to do the same thing, we would obviously want to use the more efficient solution. 

When we're talking about runtime complexity, it's always going to be in relation to how much stuff we're pushing through the algo.

1. Types of Sorting Algorithms

    *  **_Sort_** is the default algo that Python comes with. 
        
        * Sort is very efficient. It is optimized and is (most likely) the fastest algo that is practical in a language known to us at the moment. 
        
        * If you run the sort algo, it should come as no surprise that is is really, really quick. You will get a rough estimate of how many milliseconds the function took. In Artem's example, it was 0.002 ms.
        
        * Again, you'll see that it's really fast - which is great. That's what we want from our algos. 

        * Sort is sort of like the O(n) of Big O Notation. 

    * **_Insertion Sort_** sorts the array correctly and relatively fast. 
        
        * Insertion sort just isn't quite as fast as what Python comes with. It's still pretty fast, however, it is still significantly slower than what Python already comes with. In Artem's example, it was 0.04 ms (4x slower, actually). We will cover this more in later modules. 

        * You can think of Insertion Sort as kind of like the O(n^2) in Big O Notation.

    * **_Bogo Sort_** comes with many different names, such as Stupid Sort. It's a really horrible algo.  

        * The point of Bogo Sort is it will take the numbers/elements, shuffle them, and then check if it's sorted. 

        * In Artem's example, it took 0.6 ms. That is _obviously_ not great.

        * We can mostly ignore this type of sort. 

        * Bogo Sort is like the really bad one in Big O Notation - O(n!). Literally the worst. If you have an algo like this, you can't accomplish anything with it past 5 elements.

2. When we think about efficiency, the times between Sort and Insertion Sort aren't too bad _right now_. You may even think they're negligible realistically because "who cares if it takes 0.02 ms or 0.04 ms, as it almost seems like a fluke?" 

    If you add more elements into the array (say, 50 items), the regular Sort will barely be affected. In Insertion Sort, it goes up to 0.3 which is really bad considering it started at 0.04 ms. If you keep going with Insertion Sort, you will see that it's getting worse for sure. 

    We don't care about the _exact_ time that an algo takes, what we want to consider is how much slower does it get as we add more input into the algo. 
    
    Again, it's not necessarily about how long some algo takes because all computers are built differently; there might be a fluke where one time a computer runs something fast or runs something slow b/c it's doing something else. You might be running it on your cell phone or you could be running it on a super computer you licensed from AWS. 

    The time itself is not the important part. The important part is how does the algo keep performing as we put more input into it? If it goes slower and slower and slower quicker, then it becomes a worse and worse algo.

    In other words, if we were to plot - just draw a graph where the x-axis is the # of Elements and the y-axis is Time (or # of Steps). Insertion will start curving upwards fairly quickly, meaning it takes longer and longer to perform the necessary steps. Sort, on the other hand will handle the extra input much quicker. It takes Sort much longer to climb the Y-axis, as it's time needed to perform the steps are much quicker. 

    We care about the shape of the graph. We care about how fast the _number of steps_ grows given a number of elements. In you keep increasing the elements, does the function grow slower and slower and slower? 

3. Analyzing Big O is one of those skills that really, really improves over time as you keep practicing it. This is one of those skills that once you start to notice certain patterns, you kind of build an intuition for how these functions work.
    
    * How to Analyze Big O Notation:
  
        * Think about how the function will work if you change the size of the input. Does the 
        number of steps increase if the input size increases?

        * Go line by line and figure out which Big O Notation of each line is. Then add them up. 

        * If there's a loop, look at the code _inside_ the loop. 
            
            * Go line by line and determine the Big O of each line.
            
            * Then add it all together.

            * Then, we want to multiply the sum by the number of times the for loop runs in relation
            to n.
    
### Data Structures

Data structures provide: 
    
    * Data storage

    * Accessibility to the data
        
        * arr[3]

        * data_struct.read()

    * Insertion - add data to the Data Structure. Insertion adds a whole new item to the data structure. 
        
        * array.append()

        * dict["new_key"] = value

    * Deletion

    * Search through a data structure. Search is considered a core function because we often figure out if certain data is or is not in a data structure. Otherwise, why would we even use a data structure if there wasn't some kind of search involved? 

### Linked Lists

1. Linked Lists also have all of those abilities found in Data Structures as well. 
        
    * Linked Lists stores information a little differently. 

    * Consider LL as sort of linear data structures. 
        
        * Essentially, they store data in a linear way and almost usually guarantee that the data's order will be kept. 
        
        * If it's at the back of a linear data structure, it's going to stay there until you remove/add something else to the end of it.  

    * Linked lists can be thought of as a bunch of values that are literally just linked to each other. 
        
        *  Node --- Node --- Node --- Node

           | 1 |-------| 2 |-------| 3 |-------| 4 |

        * You can store whatever you want in these values

        * Each of the these values knows how to get to the next one because they are linked.

    * The OS does not need to find space large enough to fit all the items in the linked list. It will place individual nodes in individual spaces. The nodes will find each other with pointers. But you will need to know the start in order to access it.

2. Arrays are one big combined chunk and each item is right next to each other. That is not the case with LL. A LL has the distinction where each node knows how to get to the next one.

    * What's the use of LL when we can use an array? If we implement our LL properly, we may have some serious wins over some of the core functions that Data Structures have. 

    * If we wanted to delete from an array, we would have to go in, delete the item, the move the subsequent items over to get rid of the empty hole in the array. 
        
        * If the array was 1000s of items long, we would have to have to painfully move over each one of the elements over one by one. In this case, the runtime would be O(n) to delete - where n is the length of the array. It's not the worst, but it's not great either. 

        * If we need to delete a lot, then we're probably going to start to feel it. 

    * Likewise, what would it take to add an element to an array? If you wanted to insert something between 2 elements in an array, you'd need to make space between them and then move everything on the right side over a space to insert it into the array.

        * Inserting into an array would be O(n) just like deletion. Obviously, not great. 

    * If we want to find out what the 2nd element in the array is, it's going to be Constant time - O(1). 

    * With arrays, the OS is going to find a spot where it can fit **_all_** the items of the array.

3. A Linked List's node only needs to know 2 things:
    
    * The value

    * The next node

### Stacks

1. A stack is a data structure that literally mimics a stack of papers on your desk. 

2. Linear

3. Last In, First Out (LIFO)

4. Like a stack of papers on your desk. If we have a stack of papers on our desk, what do we need to be able to with that stack of papers?
    
    * Put an item on the top
    
    * Take an item off the top
    
    * Or just look at what's on top of the desk without actually taking it off the desk.

5. Example Operations:
    
    * **push(item)** - adding an item to the top of the stack
    
    * **pop()** - removing the item on the top of the stack; typically returns the item that is removed
    
    * **peek()** - returns the value of the item on the top of the stack without removing it

6. All stack operations take O(1) time.


### Queues

1. Queues are like checkout lines at the grocery store. 

2. Also linear

3. First In, First Out (FIFO)

4. Example Operations:
    
    * **enqueue(item)** - adding an item to the end of the queue
    
    * **dequeue()** - removing the item at the beginning of the queue; typically returns the item that is removed

5. All queue operations also take O(1) time. 