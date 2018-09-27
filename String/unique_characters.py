# Check if a String is composed of all unique characters
import re
import unittest

def has_unique_characters(s):
	if s is None:
		return None

	alphabet_dict = {}
	is_unique = True
	for char in s:
		if alphabet_dict.get(char) is None:
			alphabet_dict[char] = 1
		else:
			is_unique = False
			break

	if len(s) == len(alphabet_dict.keys()):
		return True

	return is_unique


class Test(unittest.TestCase):
    data = [
        [
            "Mr. Owl Ate My Metal Worm", False
        ],
        [
            " ", True
        ],
        [
            "", True
        ],
        [
        	None, None
        ],
        [
        	"qwertyuiopasdfghjklzxcvbnm", True
        ],
        [
        	"i know!", True
        ]
    ]

    def test_has_unique_characters(self):
        for item in self.data:
            actual = has_unique_characters(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()