# Check if String is a palindrome
import re
import string
import unittest


def palindrome_string(s):
	if s is None:
		return None

	is_palindrome = True

	s = re.sub('[^A-Za-z0-9]+','', s)
	s = s.lower()

	start = 0
	end = len(s) - 1
	while start <= end:
		if s[start] != s[end]:
			is_palindrome = False
			break
		start += 1
		end -= 1

	return is_palindrome


class Test(unittest.TestCase):
    data = [
        [
            "Mr. Owl Ate My Metal Worm", True
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
        	"A Man, A Plan, A Canal-Panama!", True
        ],
        [
        	"Is this a palindrome?", False
        ]
    ]

    def test_palindrome_string(self):
        for item in self.data:
            actual = palindrome_string(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()