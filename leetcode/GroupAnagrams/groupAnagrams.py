# Solution: Use canonical form as a key. Then store the words in their respective canonical key
# Complexity: Time O(n^2Log n) | Space O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        return groups.values()
            