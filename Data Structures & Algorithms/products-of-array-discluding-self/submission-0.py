'''
Brute Force: Multiply all and use Division per nums[i]

Idea:
    For every element, its product except itself is the product of everything to its right and everything to its left
    If nothing to right or left, let it be 1

Opt1:
    Create two different arrays for left and right, where left array holds prod of everything to the left of nums[i] and right does the same
    To get final product, it will be left[i] * right[i]

    Example
    nums = [1,2,4,6]
    left = [1,1,2,8]
    right = [48,24,6,1]
    final = [48,24,12,8]

Opt2:
    We do not need the left array, we can hold a running product for left and build the right array and use it with left
''' 

class Solution:
    def build_right(self, nums: List[int]) -> List[int]:
        right = [0] * len(nums)
        right[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        return right


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = self.build_right(nums)
        result = [0] * len(nums)
        
        for i, num in enumerate(nums):
            result[i] = left * right[i]
            left *= num

        return result
