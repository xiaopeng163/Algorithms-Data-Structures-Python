Stacks
===========

Stack（堆栈）是一种线性数据结构，其操作遵循先进后出（LIFO），后进先出（FILO）的原则。

Stack is a linear data structure that follows a particular order in which the operations are performed.
The order may be ``LIFO`` (Last In First Out) or ``FILO`` (First In Last Out).
LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

.. image:: ../_static/4-stacks_queues/stacks.png
   :width: 700px


operations
------------------

下面是每个操作的基本描述和时间复杂度分析：

- 入栈（push）操作：将元素压入栈顶。时间复杂度：O(1)

- 出栈（pop）操作：从栈顶弹出元素。时间复杂度：O(1)

- 查看栈顶元素（peek）操作：返回栈顶元素，但不弹出。时间复杂度：O(1)

- 判断栈是否为空（isEmpty）操作：判断栈是否为空。时间复杂度：O(1)

.. literalinclude:: ../_code/4-stacks_queues/stacks.py
   :language: python
   :linenos: