"""
方法1：排序法

首先对两个字符串分别进行排序，如果它们排序后相等，那么这两个字符串就是anagram。
"""


def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2


"""
方法2：哈希表法

可以使用哈希表来记录每个字符在字符串中出现的次数，如果两个字符串中每个字符出现的次数都相同，那么这两个字符串就是anagram。
"""

from collections import Counter


def is_anagram1(s1, s2):
    return Counter(s1) == Counter(s2)
