LeetCode 练习
================

Validate Binary Search Tree
---------------------------------

各大公司热门面试题

https://leetcode.com/problems/validate-binary-search-tree/


如何才算一个二叉搜索树？

- 当前节点的值大于其所有的左子树节点的值
- 当前节点的值小于其所有的右子树节点的值
- 当前节点的左子树和右子树也是二叉搜索树

.. image:: ../_static/6-tree/leetcode-valid-bst.PNG
   :width: 700px

常用的解题方法

- 按二叉搜索树的定义，暴力比较
- 按In order遍历这个树，然后对遍历结果进行检查，看是否是顺序排列
