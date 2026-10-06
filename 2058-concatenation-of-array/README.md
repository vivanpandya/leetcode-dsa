<h2><a href="https://leetcode.com/problems/concatenation-of-array">Concatenation of Array</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code> of length <code>n</code>, you want to create an array <code>ans</code> of length <code>2n</code> where <code>ans[i] == nums[i]</code> and <code>ans[i + n] == nums[i]</code> for <code>0 &lt;= i &lt; n</code> (<strong>0-indexed</strong>).</p>

<p>Specifically, <code>ans</code> is the <strong>concatenation</strong> of two <code>nums</code> arrays.</p>

<p>Return <em>the array </em><code>ans</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [1,2,1,1,2,1]
<strong>Explanation:</strong> The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,1]
<strong>Output:</strong> [1,3,2,1,1,3,2,1]
<strong>Explanation:</strong> The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>The required array is simply the given <code>nums</code> array repeated twice.</p>

<p>In Python, we can concatenate two arrays using the <code>+</code> operator:</p>

<pre>
nums + nums
</pre>

<p>For example:</p>

<pre>
[1,2,1] + [1,2,1]

= [1,2,1,1,2,1]
</pre>

<h3>Algorithm</h3>

<pre>
1. Take the given array nums.
2. Concatenate nums with itself using nums + nums.
3. Return the resulting array.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def getConcatenation(self, nums):
        return nums + nums
</pre>

<h3>Example</h3>

<pre>
nums = [1,2,1]

nums + nums

= [1,2,1] + [1,2,1]

= [1,2,1,1,2,1]

Answer = [1,2,1,1,2,1]
</pre>

<h3>Why This Works</h3>

<p>The problem asks us to place the entire <code>nums</code> array twice in the result.</p>

<p>The Python expression <code>nums + nums</code> creates exactly this concatenation.</p>

<p>Therefore, the resulting array contains all elements of <code>nums</code> followed by the same elements again.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We create a new array containing <code>2n</code> elements.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The new result array contains <code>2n</code> elements.</p>

<h3>Pattern</h3>

<p><strong>Array Concatenation</strong></p>
