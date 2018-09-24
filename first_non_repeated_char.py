# Find the first non-repeated character in a String
import unittest


def first_non_repeated_char(s):
	count = {}

	for item in s:
		if item not in count:
			count[item] = 0
		count[item] += 1

	for item in s:
		if count[item] == 1:
			return item

	return None


class Test(unittest.TestCase):
    data = [
        [
            "googlethis", 'l'
        ],
        [
            "123", '1'
        ],
        [
            "", None
        ],
        [
        	"aabb", None
        ],
        [
        	" ", " "
        ]
    ]

    def test_first_non_repeated_char(self):
        for item in self.data:
            actual = first_non_repeated_char(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()