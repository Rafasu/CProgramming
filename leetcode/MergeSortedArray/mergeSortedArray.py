# Solution 1: Using auxiliary extra array.
# Complexity: Time O(m + n) | Space O(m + n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mergedArray = []
        i = 0 
        j = 0
        while(i < m and j < n):
            if(nums1[i] <= nums2[j]):
                mergedArray.append(nums1[i])
                i += 1
            else:
                mergedArray.append(nums2[j])
                j += 1
        while(i < m):
            mergedArray.append(nums1[i])
            i += 1
        while(j < n):
            mergedArray.append(nums2[j])
            j += 1
        return mergedArray

# Runtime: 36 ms, faster than 57.53% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.

# Solution 2: Merging greatest number first
# Complexity:  Time O(m+n) | Space O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = (m + n) - 1
        i, j = m - 1, n - 1
        while(k >= 0):
            if(i < 0):
                nums1[k] = nums2[j]
                j -= 1
            elif(j < 0):
                return 
            else:
                if(nums1[i] >= nums2[j]):
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            k -= 1
# Runtime: 40 ms, faster than 17.69% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.

# Solution: Just taking care of nums2 pointer
# Complexity:  Time O(m+n) | Space O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = (m + n) - 1
        i, j = m - 1, n - 1
        while(j >= 0):
            if(nums1[i] >= nums2[j] and i >= 0):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# Runtime: 36 ms, faster than 57.53% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.