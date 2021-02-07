//Solution:  Using array to calculate fibonacci number
// Complexity: Time O(n) | Space O(1)

/**
 * @param {number} N
 * @return {number}
 */
var fib = function(N) {
    let twoLast = [0, 1];
    let count = 2;
    while(count <= N){
        nextFib = twoLast[0] + twoLast[1];
        twoLast[0] = twoLast[1];
        twoLast[1] = nextFib;
        count++;
    }
    return (N >= 1 ? twoLast[1]: twoLast[0]);
};

// Runtime: 56 ms, faster than 63.52% of JavaScript online submissions for Fibonacci Number.
// Memory Usage: 33.7 MB, less than 100.00% of JavaScript online submissions for Fibonacci Number.