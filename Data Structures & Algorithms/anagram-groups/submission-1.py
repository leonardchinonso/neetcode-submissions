'''
Idea:
Two words are anagrams if their freq maps are equal in terms of keys and vals.

Brute force -> For each word, just have an is_anagram() method and run the two words in this method. If true, group them. If a word is already grouped in the resulting map, add it

Opt1:
    Build a hashmap with each word's sorted form as the key. Iterate through each word and sort it, then place it in the hashmap group with the key that equals the sorted value
    Time: O(nklogk), where k is the length of the longest word in the input. and n is len(input)
    Space: O(n)

Opt2:
    Iterate over each word and build a freq map of the word. Maps are not hashable so we can use a hashable freq vector (python tuples)
    To build the freq vector, since lowercase english letters are used, we can have a vector of size 26
    For each word, build its vector and check if it is in the hashmap
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.opt2(strs)

    def opt1(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap["".join(sorted(s))].append(s)
        return list(hashmap.values())

    def opt2(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            freq_vec = self.build_freq_vec(s)
            freq_tup = tuple(freq_vec)
            hashmap[freq_tup].append(s)
        return list(hashmap.values())

    def build_freq_vec(self, s: str) -> List[int]:
        freq_vec = [0] * 26
        for c in s:
            freq_vec[ord(c) - ord('a')] += 1
        return freq_vec
'''
Dryrun

strs = ["act","pots","tops","cat","stop","hat"]
hashmap = {
    act: [act, cat]
    opst: [pots, tops, stop]
    aht: [hat]
}
s = hat
sorted = aht
returns [[act, cat], [pots, tops, stop], [hat]]


'''