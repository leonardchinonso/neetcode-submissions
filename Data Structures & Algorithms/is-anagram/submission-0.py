'''
Idea:
For two strings to be anagrams, they have to have the same letters with the same freq in both strings

- Brute force: for each string in s, delete it in t. Both strings should be empty at the end | Using a vector, time is O(n2) cause we have to look up all the time
- Opt 1: Freq map for both strings, then compare freqs of both maps - ensure same. | time is O(m+n) where m is len of s and n is len of t. Space is O(m+n)
    Case 1: check that all chars in s are in t, and all chars in t are in s. Fail if not true
    Case 2: check that the freq of each char in s is same in t. Fail if not true
- 

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.build_freq_map(s)
        t_map = self.build_freq_map(t)
        return self.count_and_compare_chars(s_map, t_map)

    def build_freq_map(self, string: str) -> dict:
        mapp = {}
        for char in string:
            if char in mapp:
                mapp[char] += 1
            else:
                mapp[char] = 1
        return mapp
    
    def count_and_compare_chars(self, map1: str, map2: str) -> bool:
        for k, v in map1.items():
            if k not in map2:
                return False
            v2 = map2[k]
            if v2 != v:
                return False
        
        for k, v in map2.items():
            if k not in map1:
                return False
            v1 = map1[k]
            if v1 != v:
                return False

        return True


'''
racecar, carrace
s_map = {
    r: 2
    a: 2
    c: 2
    e: 1
}
t_map = {
    r: 2
    a: 2
    c: 2
    e: 1
}

jar, jam
s_map = {
    j: 1
    a: 1
    r: 1
}
t_map = {
    j: 1
    a: 1
    r: m
}
'''