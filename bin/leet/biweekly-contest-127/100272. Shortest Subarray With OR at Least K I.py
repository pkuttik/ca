from typing import List


class Solution:
    # def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    #     min_len = float("inf")
    #     window_sum = 0
    #     left = 0
    #     for right in range(len(nums)):
    #         window_sum += nums[right]
    #         while window_sum >= k:
    #             min_len = min(min_len, right - left + 1)
    #             window_sum -= nums[left]
    #             left += 1
    #     return min_len if min_len != float("inf") else 0
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # nums = sorted(nums,  reverse=True)
        min_len = float("inf")
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = temp | nums[j]
                if temp >= k:
                    min_len = min(min_len, j-i+1)
        return min_len if min_len != float("inf") else -1



print(Solution().minimumSubarrayLength([1,2,3], 2))

def bitwise_or(array):
  """
  This function calculates the bitwise OR of all elements in an array.

  Args:
      array: A list of integers.

  Returns:
      The integer result of the bitwise OR operation.
  """
  # Initialize the result with 0 to ensure all bits are initially 0
  result = 0
  for num in array:
    # Use bitwise OR operator (|) to combine the result with the current element
    result |= num
  return result

# Example usage
my_array = [12, 1, 21, 2]
# or_value = bitwise_or(my_array)
# print(f"The bitwise OR of the array is: {or_value}")