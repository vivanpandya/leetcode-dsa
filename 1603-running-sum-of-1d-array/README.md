<h2><a href="https://leetcode.com/problems/running-sum-of-1d-array">Running Sum of 1d Array</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>nums</code>. We define a running sum of an array as&nbsp;<code>runningSum[i] = sum(nums[0]&hellip;nums[i])</code>.</p>

<p>Return the running sum of <code>nums</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [1,3,6,10]

<strong>Explanation:</strong>
Running sum is obtained as follows:
[1, 1+2, 1+2+3, 1+2+3+4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1]
<strong>Output:</strong> [1,2,3,4,5]

<strong>Explanation:</strong>
Running sum is obtained as follows:
[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,2,10,1]
<strong>Output:</strong> [3,4,6,16,17]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup>&nbsp;&lt;= nums[i] &lt;=&nbsp;10<sup>6</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use the <strong>Running Sum / Prefix Sum</strong> approach.</p>

<p>For every element after the first one, we add the previous running sum to the current element.</p>

<p>We can modify the original array directly:</p>

<pre>
nums[i] = nums[i] + nums[i - 1]
</pre>

<p>After this operation, each position contains the sum of all elements from index <code>0</code> up to that index.</p>

<h3>Algorithm</h3>

<pre>
1. Start from index 1.
2. Add the previous element to the current element.
3. Store the updated value in nums[i].
4. Continue until the end of the array.
5. Return nums.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums
</pre>

<h3>Example</h3>

<pre>
nums = [1,2,3,4]

Start:
[1,2,3,4]

i = 1:
nums[1] = 2 + 1 = 3
[1,3,3,4]

i = 2:
nums[2] = 3 + 3 = 6
[1,3,6,4]

i = 3:
nums[3] = 4 + 6 = 10
[1,3,6,10]

Answer = [1,3,6,10]
</pre>

<h3>Why This Works</h3>

<p>The previous element already contains the sum of all elements before the current position.</p>

<p>Therefore, by adding the previous value to the current value, we get the running sum for the current position.</p>

<p>For example:</p>

<pre>
nums = [1,2,3,4]

At index 1:
2 + 1 = 3

At index 2:
3 + 3 = 6

At index 3:
4 + 6 = 10
</pre>

<p>So the final array becomes:</p>

<pre>
[1,3,6,10]
</pre>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the input array directly and do not use an extra array.</p>

<h3>Pattern</h3>

<p><strong>Prefix Sum / Running Sum</strong></p>
