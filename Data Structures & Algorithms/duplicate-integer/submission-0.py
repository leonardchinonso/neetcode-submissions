'''
1 2 3 3 4 4  -> false

Approaches:
- Brute force -> Nested for loop per item in array - check if in array already | O(n2) time and O(1) space
- Opt 1 -> Use a set for the nested loop to check recurrence | O(n) time & O(n) space
- Opt 2 -> Sort the array and check two neighs are diff | O(nlogn) time & O(1) space
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Implementing Opt 1 above
        store = set()
        for num in nums:
            if num in store:
                return True
            store.add(num)
        return False

'''
Dry run

1 1
    store = 1
    curr = 1
    returns true

1
    store = 1
    curr = 1
    returns false

1 2 3
    store = 1 2 3
    curr = 3
    returns false

1 2 3 3
'''