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

<p>We use a <strong>Set</strong> to store all the numbers that appear in the array.</p>

<p>Then we check every number from <code>1</code> to <code>n</code>.</p>

<p>If a number is not present in the set, it is missing from the array, so we add it to the result.</p>

<p>This approach is simple and allows us to check whether a number exists in approximately <strong>O(1)</strong> time.</p>

<h3>Algorithm</h3>

<pre>
1. Create a set containing all numbers in nums.
2. Create an empty result list.
3. Loop from 1 to n.
4. If the current number is not in the set:
       Add it to the result.
5. Return the result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def findDisappearedNumbers(self, nums):
        seen = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result
</pre>

<h3>Example</h3>

<pre>
nums = [4,3,2,7,8,2,3,1]

Create a set:

seen = {1,2,3,4,7,8}

n = 8

Check numbers from 1 to 8:

1 → present
2 → present
3 → present
4 → present
5 → missing
6 → missing
7 → present
8 → present

Answer = [5,6]
</pre>

<h3>Why This Works</h3>

<p>The numbers that can appear in the array are from <code>1</code> to <code>n</code>.</p>

<p>By storing all existing numbers in a set, we can quickly check whether each number exists.</p>

<p>If a number from <code>1</code> to <code>n</code> is not in the set, that number must be missing from the array.</p>

<p>For example:</p>

<pre>
nums = [1,1]

seen = {1}

Check:

1 → present
2 → missing

Answer = [2]
</pre>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — Creating the set takes O(n), and checking all numbers from 1 to n also takes O(n).</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The <code>seen</code> set stores up to n different numbers. The returned result list is not counted as extra space according to the problem.</p>

<h3>Pattern</h3>

<p><strong>Hash Set / Lookup</strong></p>
