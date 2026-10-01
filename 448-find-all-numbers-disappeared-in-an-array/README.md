<h2><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array">Find All Numbers Disappeared in an Array</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.</p>

<hr>

<h3>Approach</h3>

<p>We use the <strong>Array Index Marking</strong> technique.</p>

<p>Every number in the array is between <code>1</code> and <code>n</code>. We can use each number as an index.</p>

<p>For every number <code>num</code>, we look at index <code>num - 1</code> and make that value negative. This marks that the number exists in the array.</p>

<p>After marking all numbers:</p>

<ul>
	<li>If <code>nums[i]</code> is positive, then <code>i + 1</code> is missing.</li>
	<li>If <code>nums[i]</code> is negative, then <code>i + 1</code> exists in the array.</li>
</ul>

<h3>Algorithm</h3>

<pre>
1. Go through every number in nums.
2. For each number num:
       Find index = num - 1.
       Make nums[index] negative.
3. Go through the array again.
4. If nums[i] is positive:
       i + 1 is missing.
5. Add all missing numbers to the result.
6. Return the result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
</pre>

<h3>Example</h3>

<pre>
nums = [4,3,2,7,8,2,3,1]

After marking the numbers:

Index:  0  1  2  3  4  5  6  7
Value: -4 -3 -2 -7  8 -2 -3 -1

The positive values are:

Index 4 → number 5
Index 5 → number 6

Answer = [5,6]
</pre>

<h3>Why This Works</h3>

<p>Each number <code>x</code> should correspond to index <code>x - 1</code>.</p>

<p>When we see a number, we mark its corresponding index as negative. This tells us that the number exists.</p>

<p>After processing the entire array, any index that is still positive represents a number that never appeared.</p>

<p>For example:</p>

<pre>
Index 4 is still positive
→ 4 + 1 = 5
→ 5 is missing

Index 5 is still positive
→ 5 + 1 = 6
→ 6 is missing
</pre>

<p>This allows us to solve the problem without creating a separate set or dictionary.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array twice, so the total work is linear.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the input array in-place. The returned result list does not count as extra space according to the problem.</p>

<h3>Pattern</h3>

<p><strong>Array Index Marking / In-Place Array</strong></p>
