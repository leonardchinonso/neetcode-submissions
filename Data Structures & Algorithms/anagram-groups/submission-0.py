'''
Idea:
Two words are anagrams if their freq maps are equal in terms of keys and vals.

Brute force -> For each word, just have an is_anagram() method and run the two words in this method. If true, group them. If a word is already grouped in the resulting map, add it

Opt1:
    Build a hashmap with each word's sorted form as the key. Iterate through each word and sort it, then place it in the hashmap group with the key that equals the sorted value
    Time: O(nklogk), where k is the length of the longest word in the input. and n is len(input)
    Space: O(n)

Opt2:
    Iterate over each word and build a 
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap["".join(sorted(s))].append(s)
        return list(hashmap.values())

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