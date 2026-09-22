'''
Brute force -> Nested for loop with inner for loop looking for the complement of the current value in the outer for loop
Opt1 -> Create a hashmap of val to index. Dup values exist so hashmap value has to be a vector | time O(n2) worst case for a value that occurs throughout the input vector
Opt2 -> Create a hashmap of val to EARLIEST index as we move through the input vector. At every current value, ask "have I seen target - currVal before?" If yes, fetch target - currVal index | time O(n), space O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for curr_idx, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], curr_idx]
            hashmap[num] = curr_idx
        return [] # should not get here ever


'''
Dryrun

inp = 3 4 5 6 ,,, target = 7
map = {3: 0, }
id = 1
diff = 3
return [0, 1]

inp = [5, 5], target = 10
map = {5: 0}
id = 1
num = 5
diff = 5
return [0, 1]

inp = [4, 4, 5, 6], target = 10
map = {4: 0}
id = 1
num = 4
diff = 6
'''