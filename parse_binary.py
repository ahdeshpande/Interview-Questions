# Write a function that prints out the binary form of an int

import unittest

def parse_binary(num):
	if type(num) != int:
		return None

	if num == 1 or num == 0:
		return num

	binary = 0
	multiplier = 1
	while num >= 2:
		rem = num % 2
		binary += rem * multiplier
		multiplier *= 10
		num = num // 2

	return binary + 1 * multiplier

class Test(unittest.TestCase):
    data = [
        [
            "abc", None
        ],
        [
            "123", None
        ],
        [
            0, 0
        ],
        [
        	1, 1
        ],
        [
        	7, 111
        ],
        [
        	43, 101011
        ],
        [
        	1024, 10000000000
        ]
    ]

    def test_parse_binary(self):
        for item in self.data:
            actual = parse_binary(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()