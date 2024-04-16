# DSA 

1. **Data Structures**:
   

   - Arrays and Strings: Understanding operations like searching, sorting, and manipulation.
   ### Example of an array in Python
   <!-- arr = [1, 2, 3, 4, 5] size is fixed -->

   ### Interview Questions:
   How do you find the duplicate elements in an array? (Use a dictionary to calculate duplicates)
   Explain the difference between arrays and linked lists. 
      (Arrays: contiguous blocks of memory, access by index is O(1), insert/delete is slow O(n))
      (Linked List: Node and pointer, flexible size, Insert/delete is fast, access by index is slow O(n))
   Implement an algorithm to reverse a string.
      def reverse_string("hello"):
         return s[::-1]
      

   - Linked Lists: Types (singly, doubly, circular), operations, and implementations.
   # Example of a singly linked list node in Python
   class ListNode:
      def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

   How do you find the middle element of a linked list? (Use two pointers one slow(1-step) & one fast(1-step))
   Implement an algorithm to reverse a linked list. (Use 3 pointers (current,prev,next) and change next pointer of each node to prev node)
   What is the difference between singly(Travese in one direction,less memory) linked lists and doubly(traverse in both direction, more mem) linked lists?


   - Stacks and Queues: Concepts, operations (push, pop, enqueue, dequeue), and applications.
   Explain the difference between a stack and a queue:
      Stack is LIFO data struct (open from top)
      Queue is FIFO data struct (open from both top/bottom)


   - Trees: 
      Binary Tree: A hierarchical data structure where each node has at most two children.
      Binary Search Tree (BST): A binary tree where the left child of a node contains values smaller than the node's value, and the right child contains values greater than the node's value.
      Tree Traversal Algorithms:
         In-order Traversal: Visit left subtree, then current node, then right subtree.
         Pre-order Traversal: Visit current node, then left subtree, then right subtree.
         Post-order Traversal: Visit left subtree, then right subtree, then current node.
      Balancing Techniques:
         AVL Trees: A self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one.
         Red-Black Trees: Another self-balancing binary search tree with additional properties to ensure balance, such as coloring nodes red or black.



2. **Algorithms**:
   - Searching Algorithms: 
      Binary search (to find target value in sorted array, divide the search interval in half)
      linear search (searhes for target in a seq order).

   - Sorting Algorithms: 
      Selection sort - finds the minimum element from the unsorted portion of the array and swaps it with the first unsorted element.
      bubble sort - repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order
      insertion sort - It iterates through the input array, removing one element each time and finding its correct position in the sorted array
      merge sort - divides the input array into 2 halves, recursively sorts each half, and then merges the sorted halves to produce the final sorted array.
      quicksort - selects a pivot element from the array and partitions the other elements into two sub-arrays according to whether they are less than or greater than the pivot

   - Recursion 
