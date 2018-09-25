# Determine if 2 Strings are anagrams
import unittest


def sum_characters(s):
	start = 0
	end = len(s) - 1

	total = 0

	while start <= end:
		total += ord(s[start])
		if start != end:
			total += ord(s[end])
		start += 1
		end -= 1

	return total

def are_strings_anagrams(str1, str2):
	if str1 is None or str2 is None:
		return False

	if len(str1) < 1 and len(str2) < 1:
		return True

	if len(str1) < 1 or len(str2) < 1:
		return False

	if len(str1) == len(str2):
		str1_sum = sum_characters(str1)
		str2_sum = sum_characters(str2)

		if str1_sum == str2_sum:
			return True
		else:
			return False
	else:
		return False


class Test(unittest.TestCase):
    data = [
        [
            "unittest", 'test', False
        ],
        [
            " ", " ", True
        ],
        [
            "", "", True
        ],
        [
        	None, None, False
        ],
        [
        	"tommarvoloriddle", "iamlordvoldemort", True
        ]
    ]

    def test_are_strings_anagrams(self):
        for item in self.data:
            actual = are_strings_anagrams(item[0], item[1])
            self.assertEqual(actual, item[2])

if __name__ == "__main__":
    unittest.main()
