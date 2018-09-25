# Implement quick sort

import unittest


def partition(arr, start, end):
    pivot = arr[start]

    left_mark = start + 1
    right_mark = end

    done = False
    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot:
            left_mark = left_mark + 1

        while arr[right_mark] >= pivot and right_mark >= left_mark:
            right_mark = right_mark -1

        if right_mark < left_mark:
            done = True
        else:
            arr[right_mark], arr[left_mark] = arr[left_mark], arr[right_mark]

    arr[right_mark], arr[start] = arr[start], arr[right_mark]

    return right_mark

def helper_function(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        helper_function(arr, start, pivot - 1)
        helper_function(arr, pivot + 1, end)

def quick_sort(arr):
    if arr is None:
        return None

    if len(arr) < 2:
        return arr

    helper_function(arr, 0, len(arr) - 1)

    return arr


class Test(unittest.TestCase):
    data = [
        [
            [3,2,1,5,4], [1,2,3,4,5]
        ],
        [
            [], [],
        ],
        [
            None, None
        ],
        [
            [5,5,5,5], [5,5,5,5]
        ],
        [
            [1,2,3], [1,2,3]
        ]
    ]

    def test_quick_sort(self):
        for item in self.data:
            actual = quick_sort(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()