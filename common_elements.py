# Find the common elements of 2 int arrays
import unittest


def common_elements(arr1, arr2):

	i = 0
	common = 0
	while i < len(arr1) - common:
		if arr1[i] in arr2:
			common += 1
			arr1[i], arr1[len(arr1) - common] = arr1[len(arr1) - common], arr1[i]
		else:
			arr1 = arr1[1:]
	return list(set(arr1))

class Test(unittest.TestCase):
    data = [
        [
            [1,2,3,4,5], [3], [3]
        ],
        [
            [], [], []
        ],
        [
            [1], [1], [1]
        ],
        [
        	[5,5,5,5], [1,2,3,4,5], [5]
        ],
        [
        	[1,2,3], [1,2,3], [1,2,3]
        ]
    ]

    def test_common_elements(self):
        for item in self.data:
            actual = common_elements(item[0], item[1])
            self.assertEqual(actual, item[2])

if __name__ == "__main__":
    unittest.main()
