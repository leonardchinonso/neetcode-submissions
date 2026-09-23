'''
Brute Force:
    Build a freq map and sort the freq map by the value, then pick the highest k keys
    Time O(nlogn), Space O(n)

Opt1: Use a heap
    Build a freq map, but don't sort it yet.
    From the map, build a tuple pair that goes into the min heap of size k
    For each insert into the min heap, the smallest value remains on top
    Take out the smallest value by comparing against the current value, this keeps the two largest values in the heap
    At the end of the inserts, keep popping until k is exhausted and return the values
'''

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = self.build_freq_map(nums)
        nodes = [(v, k) for k, v in freq_map.items()]

        for node in nodes:
            if len(heap) < k:
                heapq.heappush(heap, node)
                continue
            if node[0] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, node)
        
        return [node[1] for node in heap]



    def build_freq_map(self, nums: List[int]) -> dict[int, int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        return hashmap


'''
Dryrun

Input: nums = [1,2,2,3,3,3], k = 2
heap = (2,2), (3,3)
freqmap = {1:1, 2:2, 3:3}
nodes = 1,1 -- 2,2 -- 3,3
node = 3
returns [2,3]

Input: nums = [7,7], k = 1
heap = (2:7)
freqmap = {2:7}
nodes = 2:7
node = 
returns []

Input: nums = [1 2 3 4 5 6], k = 3
heap = (1 2 3)
freqmap = {1 2 3 4 5 6}
nodes = 1 2 3 4 5 6
node = 1,4
returns [1, 2, 3]
'''