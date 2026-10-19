//1 ≤ length of string ≤ 100
//String contains lowercase English letters only (a–z)
/*Examples
Example 1
Input:
a = "leetcode"
Output:
0
Example 2
Input:
a = "aabbc"
Output:
4 */

function a_string(a) {
  // Before submitting the code, please remove the console.log statement from this function.
    // Add your code here

    for (let i = 0; i < a.length; i++) {
        let count = 0;
        for (let j = 0; j < a.length; j++) {
            if (a[i] === a[j]) {
                count++;
            }
        }
        if (count === 1) {
            return i;
        }
    }
  return -1;
}


/* Description
Find two indices in the array such that the sum of their elements is equal to the target value.
Return the index of any one valid pair.
If no such pair exists, return -1.

Test Case 1
Input:
 arr = [2, 7, 11, 15]
 target = 9
Output:
 0
Explanation:
arr[0] + arr[1] = 2 + 7 = 9
Since the target is found using index 0 and 1, we can return the first valid index, which is 0.

Test Case 2
Input:
 arr = [4, 1, 8, 5]
 target = 9
Output:
 1
Explanation:
arr[1] + arr[2] = 1 + 8 = 9
The pair satisfies the target condition.
Returning index 1 is valid.
Constraints
2 ≤ arr.length ≤ 100
-1000 ≤ arr[i] ≤ 1000
-2000 ≤ target ≤ 2000
Examples
Example 1
Input:
a = [2, 7, 11, 15]
b = 9
Output:
0
Example 2
Input:
a = [4, 1, 8, 5]
b = 9
Output:
1*/

function find_two_indices(a, b) {
  // Before submitting the code, please remove the console.log statement from this function.
    // Add your code here

    for (let i = 0; i < a.length; i++) {
        for (let j = i + 1; j < a.length; j++) {
            if (a[i] + a[j] === b) {
                return i;
            }
        }
    }
  return -1;
}       
