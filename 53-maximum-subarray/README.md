<h2><a href="https://leetcode.com/problems/maximum-subarray">Maximum Subarray</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

<hr>

<p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>

<hr>

<h3>Approach</h3>

<p>We use <strong>Kadane's Algorithm</strong>.</p>

<p>We keep two variables:</p>

<ul>
	<li><code>current</code> → sum of the current subarray.</li>
	<li><code>maximum</code> → largest sum found so far.</li>
</ul>

<p>For every number, we have two choices:</p>

<ol>
	<li>Start a new subarray from the current number.</li>
	<li>Add the current number to the previous subarray.</li>
</ol>

<p>We choose whichever gives the bigger sum.</p>

<h3>Algorithm</h3>

<pre>
1. Set current = first number.
2. Set maximum = first number.
3. Go through the remaining numbers.
4. For each number:
       current = max(number, current + number)
5. Update maximum.
6. Return maximum.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            maximum = max(maximum, current)

        return maximum
</pre>

<h3>Example</h3>

<pre>
nums = [-2,1,-3,4,-1,2,1,-5,4]

We keep checking:

current = max(current number, previous sum + current number)

At [4,-1,2,1]:

4 + (-1) + 2 + 1 = 6

So the maximum sum is 6.
</pre>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use two variables.</p>

<h3>Pattern</h3>

<p><strong>Kadane's Algorithm</strong></p>
