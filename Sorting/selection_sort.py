# Implement selection sort

import unittest


def selection_sort(arr):
	if arr is None:
		return None
		
	for fillslot in range(len(arr) - 1, 0, -1):
		position_of_max = 0
		for location in range(1, fillslot + 1 ):
			if arr[location] > arr[position_of_max]:
				position_of_max = location
		arr[fillslot], arr[position_of_max] = arr[position_of_max], arr[fillslot]

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

    def test_selection_sort(self):
        for item in self.data:
            actual = selection_sort(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()