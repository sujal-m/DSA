from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorting each string
        groups = defaultdict(list) #create a dictionary with empty lists as values
        
        for s in strs:
            key = "".join(sorted(s)) #sorts the string
            groups[key].append(s) #sorted string as key, s in appended as value

        return list(groups.values())

##-------OPTIMAL---------##

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #optimal, count the freq of each letter and use it as key
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 #works only for lowercase alphabets
            groups[tuple(count)].append(s) #converted to tuple bcoz lists are mutable and dict key aren't
        return list(groups.values())