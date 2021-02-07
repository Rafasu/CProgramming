// Solution: Using Built Functions
let rotate = function(nums, k) {
    k = k % nums.length;
      
    while (k > 0) {
      nums.unshift(nums.pop());
      k--;
    }
};

// assumming that javascript garbage collection removes memory allocation as soon as the array is 
// spliced, this solution is O(1) and not O(k) because 
// for every k blocks of memory allocated, we are removing that amount from nums.

var rotate = function(nums, k) {
    let pos = (k % nums.length)
    let n = nums.splice(nums.length - pos)
    nums.splice(0, 0, ...n)
};

//Solution: Using Extra Array

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var rotate = function(nums, k) {
    const n = nums.length;
    let newArray = Array(n).fill(0);
    for(let i = 0 ; i < n; i++){
        newArray[(i + k )% n ] = nums[i];
    }
    
    for(let i = 0; i < n; i++){
        nums[i] = newArray[i];
    }
};


//Solution: Rotate Array
/*
Time complexity : O(n)O(n). nn elements are reversed a total of three times.
Space complexity : O(1)O(1). No extra space is used.
*/ 
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const reverse = (start, end, arr) =>{
    while(start < end){
        const temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

var rotate = function(nums, k) {
   const end =  nums.length - 1;
    k = k % nums.length; 
    reverse(0, end, nums);
    reverse(0, k-1, nums);
    reverse(k, end, nums);     
};

//Runtime: 68 ms, faster than 75.07% of JavaScript online submissions for Rotate Array.
//Memory Usage: 35.3 MB, less than 68.42% of JavaScript online submissions for Rotate Array.







