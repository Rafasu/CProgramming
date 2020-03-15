// https://leetcode.com/problems/two-sum/


//Solution: Two-pass Hash Table
/*
We reduce the look up time from O(n)O(n) to O(1)O(1) by trading space for speed. A hash table 
is built exactly for this purpose, it supports fast look up in near constant time. I say "near" 
because if a collision occurred, a look up could degenerate to O(n)O(n) time. But look up in hash 
table should be amortized O(1)O(1) time as long as the hash function was chosen carefully.
*/ 

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = new Map();
    const n = nums.length;
    for(let i = 0 ; i < n; i++){
        map.set(nums[i], i);
    }
    for(let i = 0; i < n; i++){
        const complement = target - nums[i];
        if(map.has(complement) && map.get(complement) != i){
            return [i, map.get(complement)];   
         }
    }
}; 

Runtime: 56 ms, faster than 85.49% of JavaScript online submissions for Two Sum.
Memory Usage: 36.3 MB, less than 11.16% of JavaScript online submissions for Two Sum.


// Solution: Two-pass Hash Table with JS Objects. 

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
     let map = new Object();
    for (var i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (map.hasOwnProperty(complement)) {
            return [map[complement], i]
        }
        map[nums[i]] = i;
    }
}; 
