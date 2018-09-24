# Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array.
# Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
import unittest


def is_rotated_array(arr1, arr2):

    if len(arr1) < 1 or len(arr2) < 1:
        return False

    n, i, j = len(arr1), 0, 0

    if n != len(arr2):
        return False

    while i < n and j < n:
        k = 1
        while k <= n and arr1[(i + k) % n] == arr2[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if arr1[(i + k) % n] > arr2[(j + k) % n]:
            i += k
        else:
            j += k
    return False


class Test(unittest.TestCase):
    data = [
        [
            [1,2,3,5,6,7,8], [5,6,7,8,1,2,3], True
        ],
        [
            [3,1,2,3,4], [3,4,3,1,2], True
        ],
        [
            [], [], False
        ],
        [
            [1], [1], True
        ],
        [
        	[5,5,5,5], [5,5,5,5], True
        ],
        [
        	[1,2,3,4,5], [5,2,3,3,1], False
        ]
    ]

    def test_is_rotated(self):
        for item in self.data:
            actual = is_rotated_array(item[0], item[1])
            self.assertEqual(actual, item[2])

if __name__ == "__main__":
    unittest.main()
