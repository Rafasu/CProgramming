// Solution: Using 3 pointers and adding greatest number to last place.
// Complexity: Time(m + n)| Space(1)

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = (m + n) - 1;
    while(k >= 0){
        if(i < 0){
            nums1[k] = nums2[j];
            j--;
        }
        else if(j < 0){
            return;
        }
        else{
            if(nums1[i] >= nums2[j]){
               nums1[k] = nums1[i];
                i--;
            }
            else{
                nums1[k] = nums2[j];
                j--;
            }
        }
        k--;
          
    }
};