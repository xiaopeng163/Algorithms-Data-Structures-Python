# https://leetcode.com/problems/trapping-rain-water/


def trap(height):
    # fill in
    pass


# Trapping Rain Water within given set of bars
if __name__ == "__main__":
    heights = [5, 1, 2, 4, 4, 4, 3, 1, 0, 0, 0]
    print("Maximum amount of water that can be trapped is", trap(heights))


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert trap([0, 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 0]) == 6
        print("PASSED: `trap([0,0,1,0,2,1,0,1,3,2,1,2,1,0,0])` should return `6`")

    def test_2(self):
        assert trap([0, 0, 1, 0, 2, 4, 4, 4, 2, 3, 1, 0, 2, 4, 3, 1, 0, 1]) == 14
        print(
            "PASSED: `trap([0,0,1,0,2,4,4,4,2,3,1,0,2,4,3,1,0,1])` should return `14`"
        )

    def test_3(self):
        assert trap([0, 0, 1, 2, 4, 4, 4, 3, 1, 0, 0, 0]) == 0
        print("PASSED: `trap([0,0,1,2,4,4,4,3,1,0,0,0])` should return `0`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
