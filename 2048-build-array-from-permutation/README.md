<h2><a href="https://leetcode.com/problems/build-array-from-permutation">Build Array from Permutation</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given a <strong>zero-based permutation</strong> <code>nums</code> (<strong>0-indexed</strong>), build an array <code>ans</code> of the <strong>same length</strong> where <code>ans[i] = nums[nums[i]]</code> for each <code>0 &lt;= i &lt; nums.length</code> and return it.</p>

<p>A <strong>zero-based permutation</strong> <code>nums</code> is an array of <strong>distinct</strong> integers from <code>0</code> to <code>nums.length - 1</code> (<strong>inclusive</strong>).</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,2,1,5,3,4]
<strong>Output:</strong> [0,1,2,4,5,3]
<strong>Explanation:</strong> The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,0,1,2,3,4]
<strong>Output:</strong> [4,5,0,1,2,3]
<strong>Explanation:</strong> The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
	<li>The elements in <code>nums</code> are <strong>distinct</strong>.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow-up:</strong> Can you solve it without using an extra space (i.e., <code>O(1)</code> memory)?</p>

<hr>

<h3>Approach</h3>

<p>We need to build a new array where each element is:</p>

<pre>
ans[i] = nums[nums[i]]
</pre>

<p>We traverse the array and use <code>nums[i]</code> as an index to access another element from <code>nums</code>.</p>

<p>For example, if:</p>

<pre>
nums = [0,2,1,5,3,4]
</pre>

<p>When <code>i = 1</code>:</p>

<pre>
nums[1] = 2

nums[nums[1]]
= nums[2]
= 1
</pre>

<p>So <code>ans[1] = 1</code>.</p>

<h3>Algorithm</h3>

<pre>
1. Create an empty result array.
2. Traverse every index i from 0 to n - 1.
3. Find nums[nums[i]].
4. Add this value to the result array.
5. Return the result array.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def buildArray(self, nums):
        result = []

        for i in range(len(nums)):
            result.append(nums[nums[i]])

        return result
</pre>

<h3>Example</h3>

<pre>
nums = [0,2,1,5,3,4]

i = 0:
nums[nums[0]]
= nums[0]
= 0

i = 1:
nums[nums[1]]
= nums[2]
= 1

i = 2:
nums[nums[2]]
= nums[1]
= 2

i = 3:
nums[nums[3]]
= nums[5]
= 4

i = 4:
nums[nums[4]]
= nums[3]
= 5

i = 5:
nums[nums[5]]
= nums[4]
= 3

Answer = [0,1,2,4,5,3]
</pre>

<h3>Why This Works</h3>

<p>The problem directly defines every element of the answer as <code>nums[nums[i]]</code>.</p>

<p>For each index <code>i</code>, we first get <code>nums[i]</code>. This value is then used as another index to access the required value from <code>nums</code>.</p>

<p>By performing this for every index, we build the complete <code>ans</code> array.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array once, and each lookup takes <code>O(1)</code> time.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — We create a separate <code>result</code> array containing <code>n</code> elements.</p>

<h3>Pattern</h3>

<p><strong>Array Indexing / Nested Indexing</strong></p>
