# Classic solution for merging two sorted arrays/list to a new one.
# (Based on Merge Sort)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        m->Size of nums1 list
        n->Size of nums2 list
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