# Implement selection sort

import unittest


def insertion_sort(arr):
    if arr is None:
        return None

    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value

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

    def test_insertion_sort(self):
        for item in self.data:
            actual = insertion_sort(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()