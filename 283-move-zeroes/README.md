<h2><a href="https://leetcode.com/problems/move-zeroes">Move Zeroes</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code>, move all <code>0</code>'s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<strong>Follow up:</strong> Could you minimize the total number of operations done?

<hr>

<h3>Approach</h3>

<p>We use an <strong>index</strong> to keep track of where the next non-zero number should go.</p>

<p>First, we move all non-zero numbers to the front of the array in their original order.</p>

<p>After that, we fill all the remaining positions with <code>0</code>.</p>

<h3>Algorithm</h3>

<pre>
1. Set index = 0.
2. Go through every number in the array.
3. If the number is not 0:
       Put it at nums[index].
       Increase index.
4. After moving all non-zero numbers,
   fill the remaining positions with 0.
5. The array is now updated.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def moveZeroes(self, nums):
        index = 0

        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        while index &lt; len(nums):
            nums[index] = 0
            index += 1
</pre>

<h3>Example</h3>

<pre>
nums = [0,1,0,3,12]

Move non-zero numbers to the front:

1 → [1,1,0,3,12]
3 → [1,3,0,3,12]
12 → [1,3,12,3,12]

Now fill the remaining positions with 0:

[1,3,12,0,0]
</pre>

<h3>Why This Works</h3>

<p>We keep all non-zero numbers in the same order and put them at the beginning.</p>

<p>Once all non-zero numbers are placed, every remaining position can simply be changed to <code>0</code>.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array a constant number of times.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the original array and do not create another array.</p>

<h3>Pattern</h3>

<p><strong>Two Pointer / In-Place Array</strong></p>
