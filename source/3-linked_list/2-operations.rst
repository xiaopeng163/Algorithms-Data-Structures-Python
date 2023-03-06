Operations
==============

和Array对比一下


====================== =============== ========================================== ============================
Operations              Big-O (Array)    Big-O (singly linked list)                Big-O (doubly linked list)
====================== =============== ========================================== ============================
任意位置元素访问             O(1)           O(n)                                      O(n)
头部插入/删除               O(n)            O(1)                                      O(1)
尾部插入/删除               O(1)           O(1)，或者O(n)（取决于是否知道尾部）            O(1)
任意位置插入删除             O(n)           O(n)                                       O(n)
====================== =============== ========================================== ============================

Linked Lists Advantages
-------------------------

linked list is dynamic data structure, it can grow and shrink in size during runtime. 操作第一个元素的速度非常快。

Linked Lists Disadvantages
----------------------------

- need more memory to store the pointer to the next node
- need to traverse the list to find the last node， so the time complexity is O(n)
- can not go backwards, so it is not possible to find the previous node


Linked List vs Array
----------------------

1）动态和静态

Linked list is dynamic, array is static.

2）Random Access

Array的元素是紧挨着的，所以可以通过index快速来访问，而linked list的元素是分散的，所以需要遍历整个list来访问。

3）插入第一个元素

Array需要移动所有的元素，所以时间复杂度是O(n)，而linked list只需要改变head的指针，所以时间复杂度是O(1)。

4）插入最后一个元素

Array只需要改变tail的指针，所以时间复杂度是O(1)，而linked list需要遍历整个list，所以时间复杂度是O(n)。

5）内存

Array不需要额外的内存，Linked list需要额外的内存来存储指向下一个元素的指针。
