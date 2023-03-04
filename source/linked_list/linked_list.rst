Linked Lists
==============

链表（Linked List）是一种常见的数据结构，用于存储一系列元素，每个元素由一个值和一个指向下一个元素的指针组成。

链表可以分为单向链表和双向链表。在单向链表中，每个节点都只有一个指针，指向下一个节点；而在双向链表中，每个节点都有两个指针，一个指向前一个节点，一个指向后一个节点。

.. code-block:: none

    +---+     +---+     +---+     +---+
    | 1 | --> | 2 | --> | 3 | --> |   |
    +---+     +---+     +---+     +---+


operations
-------------

- remove node at the begginning of the list O(1)
- remove node at the end of the list O(n)
- remove node at the middle of the list O(n)
- add node at the begginning of the list O(1)
- add node at the end of the list O(n)


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
