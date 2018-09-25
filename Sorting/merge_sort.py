# Implement merge sort

import unittest


def merge_sort(arr):
    if arr is None:
        return None

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

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

    def test_merge_sort(self):
        for item in self.data:
            actual = merge_sort(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()