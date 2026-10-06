<h2><a href="https://leetcode.com/problems/maximum-product-difference-between-two-pairs">Maximum Product Difference Between Two Pairs</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>The <strong>product difference</strong> between two pairs <code>(a, b)</code> and <code>(c, d)</code> is defined as <code>(a * b) - (c * d)</code>.</p>

<ul>
	<li>For example, the product difference between <code>(5, 6)</code> and <code>(2, 7)</code> is <code>(5 * 6) - (2 * 7) = 16</code>.</li>
</ul>

<p>Given an integer array <code>nums</code>, choose four <strong>distinct</strong> indices <code>w</code>, <code>x</code>, <code>y</code>, and <code>z</code> such that the <strong>product difference</strong> between pairs <code>(nums[w], nums[x])</code> and <code>(nums[y], nums[z])</code> is <strong>maximized</strong>.</p>

<p>Return <em>the <strong>maximum</strong> such product difference</em>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,6,2,7,4]
<strong>Output:</strong> 34
<strong>Explanation:</strong> We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,5,9,7,4,8]
<strong>Output:</strong> 64
<strong>Explanation:</strong> We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We first <strong>sort the array</strong> in ascending order.</p>

<p>After sorting:</p>

<pre>
nums[0]  → smallest
nums[1]  → second smallest

nums[-2] → second largest
nums[-1] → largest
</pre>

<p>Since all numbers are positive, the maximum product difference is obtained by multiplying the two largest numbers and subtracting the product of the two smallest numbers.</p>

<p>Therefore:</p>

<pre>
(largest * second_largest) - (smallest * second_smallest)
</pre>

<h3>Algorithm</h3>

<pre>
1. Sort nums in ascending order.
2. Take nums[0] and nums[1] as the two smallest numbers.
3. Take nums[-2] and nums[-1] as the two largest numbers.
4. Calculate:

       (nums[-1] * nums[-2]) - (nums[0] * nums[1])

5. Return the result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def maxProductDifference(self, nums):
        nums.sort()

        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
</pre>

<h3>Example</h3>

<pre>
nums = [5,6,2,7,4]

After sorting:

[2,4,5,6,7]

Smallest two:
2, 4

Largest two:
6, 7

Product difference:

(7 * 6) - (2 * 4)
= 42 - 8
= 34

Answer = 34
</pre>

<h3>Why This Works</h3>

<p>All numbers in the array are positive.</p>

<p>After sorting, the two largest numbers are at the end of the array and the two smallest numbers are at the beginning.</p>

<p>To maximize the difference, we want the largest possible product for the first pair and the smallest possible product for the second pair.</p>

<p>Therefore, we calculate:</p>

<pre>
(largest * second_largest) - (smallest * second_smallest)
</pre>

<p>Python's negative indexing makes it easy to access the last two elements:</p>

<pre>
nums[-1] → largest
nums[-2] → second largest
</pre>

<h3>Time Complexity</h3>

<p><strong>O(n log n)</strong> — Sorting the array takes <code>O(n log n)</code> time.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> auxiliary space — The array is sorted in-place and we only use a few variables.</p>

<h3>Pattern</h3>

<p><strong>Sorting / Find Two Smallest and Two Largest</strong></p>
