# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
import unittest


def sum_to_ten(arr):
	compliment = set()
	result = []
	sum_val = 10
	for item in arr:
		diff = sum_val - item
		if diff in compliment:
			result.append((diff, item))
			compliment.remove(diff)
		else:
			compliment.add(item)
	return result

class Test(unittest.TestCase):
    data = [
        [
            [1,2,3,4,5,6,7,8,9], [(4, 6), (3, 7), (2, 8), (1, 9)]
        ],
        [
            [], []
        ],
        [
            [1], []
        ],
        [
        	[5,5,5,5], [(5,5), (5,5)]
        ]
    ]

    def test_most_frequent(self):
        for item in self.data:
            actual = sum_to_ten(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()