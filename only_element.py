# Find the only element in an array that only occurs once.

import unittest


def only_element(arr):

	if arr is None or len(arr) < 1:
		return None

	repeated = {
	0: set(),
	1: set()
	}

	for elem in arr:
		if elem not in repeated.get(0):
			if elem in repeated.get(1):
				repeated.get(1).remove(elem)
				repeated.get(0).add(elem)
			else:
				repeated.get(1).add(elem)
	return list(repeated.get(1))


class Test(unittest.TestCase):
    data = [
        [
            [1,1,2,2,3,4,4,5,5], [3]
        ],
        [
            [], None
        ],
        [
            [1], [1]
        ],
        [
        	[5,5,5,5], []
        ],
        [
        	[1,2,3], [1,2,3]
        ]
    ]

    def test_most_frequent(self):
        for item in self.data:
            actual = only_element(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()

