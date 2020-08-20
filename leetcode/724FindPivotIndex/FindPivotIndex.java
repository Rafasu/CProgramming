/* Solution: My First solution was to use to arrays to calculate left and right sums but then I figured out
that we can calculate leftsum and rightsum with the total sum and substracting each side values
Complexity: Time O(n) | Space O(1) */

class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0, leftSum = 0, n = nums.length;
        for(int num :  nums){
            total += num;
        }
        for(int i = 0 ; i < n; i++){
            if(leftSum == total - leftSum - nums[i]){
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}