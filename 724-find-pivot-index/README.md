<h2><a href="https://leetcode.com/problems/find-pivot-index">Find Pivot Index</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array of integers <code>nums</code>, calculate the <strong>pivot index</strong> of this array.</p>

<p>The <strong>pivot index</strong> is the index where the sum of all the numbers <strong>strictly</strong> to the left of the index is equal to the sum of all the numbers <strong>strictly</strong> to the index's right.</p>

<p>If the index is on the left edge of the array, then the left sum is <code>0</code> because there are no elements to the left. This also applies to the right edge of the array.</p>

<p>Return <em>the <strong>leftmost pivot index</strong></em>. If no such index exists, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,3,6,5,6]
<strong>Output:</strong> 3

<strong>Explanation:</strong>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> -1

<strong>Explanation:</strong>
There is no index that satisfies the conditions in the problem statement.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,-1]
<strong>Output:</strong> 0

<strong>Explanation:</strong>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>Note:</strong> This question is the same as 1991: <a href="https://leetcode.com/problems/find-the-middle-index-in-array/">Find the Middle Index in Array</a></p>

<hr>

<h3>Approach</h3>

<p>We use the <strong>Total Sum + Left Sum</strong> approach.</p>

<p>First, calculate the total sum of the entire array.</p>

<p>Then, traverse the array from left to right.</p>

<p>For every index, the right sum can be calculated using:</p>

<pre>
right_sum = total_sum - left_sum - nums[i]
</pre>

<p>If <code>left_sum</code> is equal to <code>right_sum</code>, then the current index is the pivot index.</p>

<p>We traverse from left to right, so the first valid index is automatically the <strong>leftmost pivot index</strong>.</p>

<h3>Algorithm</h3>

<pre>
1. Calculate the total sum of nums.
2. Initialize left_sum = 0.
3. Traverse the array from left to right.
4. For every index i:
       Calculate right_sum:
       right_sum = total_sum - left_sum - nums[i]
5. If left_sum == right_sum:
       Return i.
6. Add nums[i] to left_sum.
7. If no pivot index is found, return -1.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
</pre>

<h3>Example</h3>

<pre>
nums = [1,7,3,6,5,6]

total_sum = 28
left_sum = 0

Index 0:
right_sum = 28 - 0 - 1
          = 27

left_sum = 1

Index 1:
right_sum = 28 - 1 - 7
          = 20

left_sum = 8

Index 2:
right_sum = 28 - 8 - 3
          = 17

left_sum = 11

Index 3:
right_sum = 28 - 11 - 6
          = 11

left_sum = 11
right_sum = 11

Answer = 3
</pre>

<h3>Why This Works</h3>

<p>The total sum contains every element in the array.</p>

<p>For the current index, we remove the current element and the elements on the left from the total sum. What remains is the sum of the elements on the right.</p>

<pre>
right_sum = total_sum - left_sum - nums[i]
</pre>

<p>Therefore, when:</p>

<pre>
left_sum == right_sum
</pre>

<p>the current index is a valid pivot index.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We calculate the total sum and traverse the array once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use a few variables and do not create any extra data structure.</p>

<h3>Pattern</h3>

<p><strong>Prefix Sum / Left Sum + Total Sum</strong></p>
