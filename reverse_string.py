# Reverse a String iteratively and recursively

import unittest

"""
g oogle
oogle g
o ogle
ogle o g
gle o o g
le  g o o g
e l g o o g
"""
def reverse_string_iter(s):
	
	if s is None:
		return None

	s = list(s)
	start = 0
	end = len(s) - 1

	while start <= end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

	return ''.join(s)


def reverse_string_recur(s):
	if s is None:
		return None
		
	if len(s) < 2:
		return s

	if len(s) == 2:
		return ''.join(s[1] + s[0])

	return ''.join(reverse_string_recur(s[1:]) + s[0])


class Test(unittest.TestCase):
    data = [
        [
            "google", 'elgoog'
        ],
        [
            " ", " "
        ],
        [
            "", ""
        ],
        [
        	None, None
        ],
        [
        	"unit test", "tset tinu"
        ]
    ]

    def test_reverse_string_iter(self):
        for item in self.data:
            actual = reverse_string_iter(item[0])
            self.assertEqual(actual, item[1])

    def test_reverse_string_recur(self):
        for item in self.data:
            actual = reverse_string_recur(item[0])
            self.assertEqual(actual, item[1])

if __name__ == "__main__":
    unittest.main()
