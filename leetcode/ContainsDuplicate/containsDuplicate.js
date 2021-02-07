// Solution: Build a frequency table
// Complexity: Time O(n) | Space O(n)
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let map = new Map();
    const n = nums.length;
    //Needed because in a forEach method, the only way to exit is throwing an exception
    let answer = false;
    for (let i = 0; i < n; i++){
        if(map.has(nums[i])){
            const iFreq = map.get(nums[i]) + 1;
            map.set(nums[i], iFreq);   
        }
        else{
            map.set(nums[i], 1);
        }
    }
    map.forEach((value, key)=>{
        if(value > 1)
            answer = true;
    });
    return answer;
};

// Runtime: 64 ms, faster than 83.25% of JavaScript online submissions for Contains Duplicate.
// Memory Usage: 42.5 MB, less than 17.65% of JavaScript online submissions for Contains Duplicate.

// Solution: Build a Hash Table 
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let map = new Map();
    const n = nums.length;
    for (let i = 0; i < n; i++){
        if(map.has(nums[i])){
           return true;   
        }
        else{
            map.set(nums[i], 1);
        }
    }
    return false;
};

//Runtime: 68 ms, faster than 71.41% of JavaScript online submissions for Contains Duplicate.
//Memory Usage: 41.1 MB, less than 61.76% of JavaScript online submissions for Contains Duplicate.
/*
There are many data structures commonly used as dynamic sets such as Binary Search Tree 
and Hash Table. The operations we need to support here are search() and insert(). For a 
self-balancing Binary Search Tree (TreeSet or TreeMap in Java), search() and insert() are 
both O(\log n)O(logn) time. For a Hash Table (HashSet or HashMap in Java), search() and insert() 
are both O(1)O(1) on average. Therefore, by using hash table, we 
can achieve linear time complexity for finding the duplicate in an unsorted array. */
