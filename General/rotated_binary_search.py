# Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
import unittest

def rotated_binary_search(arr, num):
	if arr is None or len(arr) < 1:
		return None

	pivot = find_pivot(arr)

	if pivot == 0 or arr[0] <= num:
		return binary_search(arr, 0, pivot + 1, num)

	return binary_search(arr, pivot + 1, len(arr) - 1, num)


def binary_search(arr, start, end, num):
	while start <= end:
		mid = (start + end)//2
		if arr[mid] < num:
			start = mid + 1
		elif arr[mid] > num:
			end = mid - 1
		else:
			return mid
	return -1

def find_pivot(arr):
	start = 0
	end = len(arr) - 1

	while start <= end:
		if start == end:
			return start

		mid = (start+end)//2
		if mid == 0 or arr[mid-1] < arr[mid] > arr[mid+1]:
			return mid
		elif arr[mid-1] < arr[mid] < arr[mid+1]:
			start = mid + 1
		else:
			end = mid - 1
	return 0
				
class Test(unittest.TestCase):
    data = [
        [[2], 2, 0],
		[[1,2], 2, 1],
		[[0,1,2,3,4,5], 1, 1],
		[[1,2,3,4,5,0], 0, 5],
		[[9,12,17,2,4,5], 17, 2],
		[[9,12,17,2,4,5,6], 4, 4],
    ]

    def test_rotated_binary_search(self):
        for item in self.data:
            actual = rotated_binary_search(item[0], item[1])
            self.assertEqual(actual, item[2])

if __name__ == "__main__":
    unittest.main()
