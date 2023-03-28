Queues
===========

A Queue is defined as a linear data structure that is open at both ends and the operations are performed in First In First Out (``FIFO``) order.


.. image:: ../_static/4-stacks_queues/queues.png
   :width: 700px

Queue的操作
----------------

- 入队（enqueue）操作：将元素加入队尾。时间复杂度：O(1)

- 出队（dequeue）操作：从队头弹出元素。时间复杂度：O(1)

- 查看队头元素（peek）操作：返回队头元素，但不弹出。时间复杂度：O(1)

- 判断队列是否为空（isEmpty）操作：判断队列是否为空。时间复杂度：O(1)

.. literalinclude:: ../_code/4-stacks_queues/queues.py
   :language: python
   :linenos: