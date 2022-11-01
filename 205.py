# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true
 
# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

def main():
    s = "badc"
    t = "baba"
    print(isIsomorphic(s, t))

def isdumb(s: str, t: str) -> bool:
    # both strings should be equal in length
    # each char in a string should uniquely map to another char in the other string
    
    # check size, compare, if different return false
    if len(s) != len(t):
        return False

    # put both words in sets, if sizes now different, return false
    if len(set(s)) != len(set(t)):
        return False

    new_s = ""
    # loop through word s (old_s) and swap with the same position in word t in a new variable new_s
    for i, c in enumerate(s):
        # if the char we're taking from t is already in new_s, 
        if t[i] in new_s:
            # check the position of that already in new_s char in the old_s
            position = new_s.index(t[i])
            print(position)
            print(t[position])
            print(c)
            print(s[position])
            # and check if the old_s char is the same as the current one we're in the loop
            if t[position] == t[i]:
                new_s += t[i]
            # if yes, swap and keep going
            # if no, return false
            else:
                return False
        # if not just swap it and keep going
        else:
            new_s += t[i]

    return True


# an actual solution
def isIsomorphic(s, t):
    # iterate over both strings and add each mapping into two dicts
    # confirm each time if that mapping is already on dict
    # if the key is already there but the value that would be added is different, then return false

    s_d = {}
    t_d = {}

    # loop through the strings
    for i, c in enumerate(s):
        # check if current char is in dict t
        if c in s_d:
            # if yes, then check if the value of that key in the dict is equal to current iterable char
            if s_d[c] == t[i]:
                # do nothing
                # print("It's already mapped")
                pass
            # if key value pair is diff, then return false
            else:
                # print("mapped but wrong value")
                return False
        elif t[i] in t_d:
            return False
        
        else:
            # if no, then add it to the dictionary along with value (opposite string char)
            s_d[c] = t[i]
            t_d[t[i]] = c

    return True

# the leetcode solution:
def isIsomorphicButBetter(self, s: str, t: str) -> bool:
        
        mapping_s_t = {}
        mapping_t_s = {}
        
        for c1, c2 in zip(s, t):
            
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
            
        return True

main()