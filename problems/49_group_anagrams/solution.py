from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return list(anagrams.values())

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(sol.groupAnagrams([""]))  # Expected: [[""]]
    print(sol.groupAnagrams(["a"]))  # Expected: [["a"]] 