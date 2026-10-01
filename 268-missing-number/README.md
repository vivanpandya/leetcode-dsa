<h2><a href="https://leetcode.com/problems/missing-number">Missing Number</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em></p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2

<strong>Explanation:</strong>
n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number because it does not appear in nums.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2

<strong>Explanation:</strong>
n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number because it does not appear in nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8

<strong>Explanation:</strong>
n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number because it does not appear in nums.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?</p>

<hr>

<h3>Approach</h3>

<p>We use the <strong>sum of numbers</strong> formula.</p>

<p>The array contains numbers from <code>0</code> to <code>n</code>, but one number is missing.</p>

<p>The sum of all numbers from <code>0</code> to <code>n</code> is:</p>

<pre>
n * (n + 1) // 2
</pre>

<p>We calculate the expected sum and subtract the actual sum of the array.</p>

<p>The remaining value is the missing number.</p>

<h3>Algorithm</h3>

<pre>
1. Find n using the length of the array.
2. Calculate the expected sum of numbers from 0 to n.
3. Calculate the actual sum of all numbers in nums.
4. Subtract the actual sum from the expected sum.
5. Return the result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum
</pre>

<h3>Example</h3>

<pre>
nums = [3,0,1]

n = 3

Expected numbers:
0, 1, 2, 3

Expected sum:
3 * (3 + 1) // 2
= 6

Actual sum:
3 + 0 + 1
= 4

Missing number:
6 - 4
= 2

Answer = 2
</pre>

<h3>Why This Works</h3>

<p>The complete range should contain every number from <code>0</code> to <code>n</code>.</p>

<p>When we calculate the expected sum, it includes the missing number. The actual array sum does not include it.</p>

<p>Therefore:</p>

<pre>
Expected Sum - Actual Sum = Missing Number
</pre>

<p>For example:</p>

<pre>
Expected Sum = 6
Actual Sum   = 4

6 - 4 = 2
</pre>

<p>So the missing number is <code>2</code>.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array once to calculate its sum.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use a few variables and do not create any extra data structure.</p>

<h3>Pattern</h3>

<p><strong>Math / Array Sum</strong></p>
