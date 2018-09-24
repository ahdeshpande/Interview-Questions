# Implement bubble sort
import unittest


def bubble_sort(arr):
	if arr is None:
		return None

	for i in range(0, len(arr)):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

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

    def test_bubble_sort(self):
        for item in self.data:
            actual = bubble_sort(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()