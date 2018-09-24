# Find the most frequent integer in an array


# 1, 2, 3, 4, 5, 5, 5, 4, 2, 6, 7, 2, 8


# O(n log n)
# O(n)

import unittest


def most_frequent(arr):
    if arr is None or len(arr) < 1:
        return None

    arr.sort() # O(n log n) and O(n)

    max_counter = 0
    counter = 0
    max_number = arr[0]

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            counter += 1
        else:
            if counter > max_counter:
                max_counter = counter
                max_number = arr[i]
            else:
                counter = 0

    return max_number


class Test(unittest.TestCase):
    data = [
        [
            [1, 2, 3, 4, 5, 5, 5, 4, 2, 6, 7, 8], 5
        ],
        [
            [], None
        ],
        [
            [1], 1
        ]
    ]

    def test_most_frequent(self):
        for item in self.data:
            actual = most_frequent(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()