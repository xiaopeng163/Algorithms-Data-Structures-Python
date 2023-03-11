Algorithms and Complexities
================================


Algorithm
-----------

An algorithm is a finite set of instructions, those if followed, accomplishes a particular task. It is not language specific, we can use any language and symbols to represent instructions.

一个算法是一组有限的指令，如果按照它们所规定的顺序执行，可以完成特定的任务。它不受语言限制，我们可以使用任何语言和符号来表示指令

The criteria of an algorithm
--------------------------------

算法是解决问题或实现特定任务的逐步过程。为了被认为是算法，该过程必须满足以下几个标准：

- 清晰明确：算法的每一步必须清晰明确，没有解释或混淆的余地。
- 有限性：算法必须在有限步骤后终止，这意味着它不能无限运行或无限循环。
- 输入：算法必须有一个或多个输入，这些是算法在执行任务时使用的初始数据或信息。
- 输出：算法必须有一个或多个输出，这些是算法在完成任务后产生的结果或解决方案。
- 有效性：算法必须是有效的，这意味着它应该能够在合理的时间内为任何有效输入产生正确的输出。
- 一般性：算法应该足够通用，以适用于广泛的相似问题，而不是针对单个问题或情况而设计。

这些标准有助于确保算法定义良好、可靠，并对解决特定问题或任务有用。


Analysis of algorithms
----------------------------

Algorithm analysis is an important part of computational complexities. The complexity theory provides the theoretical estimates for the resources needed by an algorithm to solve any computational task. Analysis of the algorithm is the process of analyzing the problem-solving capability of the algorithm in terms of the time and size required (the size of memory for storage while implementation). However, the main concern of the analysis of the algorithm is the required time or performance.

算法分析是计算复杂性的重要组成部分.
复杂性理论为算法解决任何计算任务所需的资源提供了理论估计。
算法分析是指通过时间和空间的需求（实现时所需的存储空间）来分析算法的问题解决能力的过程。然而，算法分析的主要关注点是所需的时间或性能

Complexities of an Algorithm
-------------------------------

The complexity of an algorithm computes the amount of time and spaces required by an algorithm for an input of size (n). The complexity of an algorithm can be divided into two types. The time complexity and the space complexity.

算法的复杂度计算的是算法在输入规模为n时所需的时间和空间。算法的复杂度可以分为两种类型：时间复杂度和空间复杂度。

Time Complexity of an Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The time complexity is defined as the process of determining a formula for total time required towards the execution of that algorithm. This calculation is totally independent of implementation and programming language.

时间复杂度是指确定执行该算法所需总时间的过程。这个计算完全独立于具体的实现和编程语言。

Space Complexity of an Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Space complexity is defining as the process of defining a formula for prediction of how much memory space is required for the successful execution of the algorithm. The memory space is generally considered as the primary memory.

空间复杂度是指定义一种公式来预测算法在成功执行时需要多少内存空间的过程。通常，内存空间是指主存储器。

.. warning::

    无法准确地测量算法的运行时间，因为算法所需的时间取决于它执行的硬件和软件环境。

    我们应该测量算法执行的操作次数。操作次数是算法所需时间的良好近似值

https://en.wikipedia.org/wiki/Algorithm


常用算法
------------


Search 搜索
~~~~~~~~~~~~~~~~~~~~~

例如 Binary search （二分查找）

著名的 BFS（广度优先） DFS（深度优先）

Sorting 排序
~~~~~~~~~~~~~~~~~~~~~~~~~

例如 Bubble sort （冒泡排序）

