'''
Idea:
We know len of each str in the input vector is 200 at most
So we can prepend each string with YYY, where each Y is a digit and the length of the next string to take in.
So [HolidayJourney, Eatery] turns to 014HolidayJourney006Eatery
'''

def transform_str_with_length(s: str) -> str:
    k = str(len(s))
    if len(k) == 1:
        return "00" + k + s
    if len(k) == 2:
        return "0" + k + s
    return k + s

def get_start_end(s: str, pos: int) -> (int, int):
    '''
    pos = 0, s = "005April"
    k => int(s[005]) => 5
    return 3, 8 ["April"]
    '''
    new_pos = pos+3
    k = int(s[pos:new_pos])
    return new_pos, new_pos+k


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += transform_str_with_length(s)
        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        pos = 0
        result = []

        while pos < len(s):
            start, end = get_start_end(s, pos)
            result.append(s[start:end])
            pos = end

        return result

'''
Input: strs = ["Hello","World!"]
encode()
    result = "" + 005 + Hello => 005Hello
    result = "005Hello" + 006 + World! => 005Hello006World!
decode()
    s = "005Hello006World!"
    pos = 8
    res = ["Hello", "World!"]
    len = 17
    start, end = get_start_end(005Hello006World!, 8)
        pos = 8
        newpos = 11
        k = int(006) => 6
        return 11, 17
    start, end = 11, 17
    
'''
