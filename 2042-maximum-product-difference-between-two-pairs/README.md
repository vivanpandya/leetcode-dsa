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

<p>To maximize the product difference, we need the <strong>two largest numbers</strong> for the first product and the <strong>two smallest numbers</strong> for the second product.</p>

<p>Instead of sorting the array, we find these four values in a single traversal.</p>

<p>We keep track of:</p>

<pre>
smallest
second_smallest
largest
second_largest
</pre>

<p>Then the answer is:</p>

<pre>
(largest * second_largest) - (smallest * second_smallest)
</pre>

<h3>Algorithm</h3>

<pre>
1. Initialize smallest and second_smallest to infinity.
2. Initialize largest and second_largest to negative infinity.
3. Traverse every number in nums.
4. Update the two smallest values.
5. Update the two largest values.
6. Calculate:

       (largest * second_largest) - (smallest * second_smallest)

7. Return the result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def maxProductDifference(self, nums):
        smallest = float('inf')
        second_smallest = float('inf')

        largest = float('-inf')
        second_largest = float('-inf')

        for num in nums:
            if num &lt;= smallest:
                second_smallest = smallest
                smallest = num
            elif num &lt; second_smallest:
                second_smallest = num

            if num &gt;= largest:
                second_largest = largest
                largest = num
            elif num &gt; second_largest:
                second_largest = num

        return (largest * second_largest) - (smallest * second_smallest)
</pre>

<h3>Example</h3>

<pre>
nums = [5,6,2,7,4]

Smallest two:
2, 4

Largest two:
6, 7

Product difference:

(6 * 7) - (2 * 4)
= 42 - 8
= 34

Answer = 34
</pre>

<h3>Why This Works</h3>

<p>All numbers in the array are positive.</p>

<p>Therefore, to make the first product as large as possible, we choose the <strong>two largest numbers</strong>.</p>

<p>To make the second product as small as possible, we choose the <strong>two smallest numbers</strong>.</p>

<p>By finding these four values in one traversal, we get the maximum possible product difference without sorting the array.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use four variables to track the smallest and largest values.</p>

<h3>Pattern</h3>

<p><strong>One Pass / Find 2 Smallest and 2 Largest</strong></p>
