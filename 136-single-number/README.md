<h2><a href="https://leetcode.com/problems/single-number">Single Number</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,1]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use the <strong>XOR</strong> operator.</p>

<p>The important XOR rules are:</p>

<pre>
a ^ a = 0
a ^ 0 = a
</pre>

<p>Every number appears twice except one. When we XOR all the numbers, the duplicate numbers cancel each other.</p>

<p>For example:</p>

<pre>
4 ^ 1 ^ 2 ^ 1 ^ 2

= 4 ^ (1 ^ 1) ^ (2 ^ 2)

= 4 ^ 0 ^ 0

= 4
</pre>

<p>Therefore, the number that appears only once remains as the final result.</p>

<h3>Algorithm</h3>

<pre>
1. Initialize result = 0.
2. Traverse every number in nums.
3. XOR the current number with result.
4. Store the XOR value back in result.
5. After processing all numbers, return result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result
</pre>

<h3>Example</h3>

<pre>
nums = [4,1,2,1,2]

Start:
result = 0

0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4

Answer = 4
</pre>

<h3>Why This Works</h3>

<p>Every duplicate number appears exactly twice.</p>

<p>When the same number is XORed with itself, it becomes <code>0</code>.</p>

<pre>
1 ^ 1 = 0
2 ^ 2 = 0
</pre>

<p>The single number is never cancelled because it appears only once.</p>

<p>Therefore, after XORing all elements, only the single number remains.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use the <code>result</code> variable.</p>

<h3>Pattern</h3>

<p><strong>XOR / Bit Manipulation</strong></p>
