<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>You are given an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>

<strong>Follow-up:</strong> Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code> time complexity?

<hr>

<h3>Approach</h3>

<p>We use a <strong>HashMap (Dictionary)</strong> to store the numbers we have already seen and their indices.</p>

<p>For every number:</p>

<ol>
	<li>Find the number we need: <code>needed = target - current number</code></li>
	<li>Check if <code>needed</code> is already in the HashMap.</li>
	<li>If it is present, we found the two numbers, so return their indices.</li>
	<li>If it is not present, store the current number and its index in the HashMap.</li>
</ol>

<h3>Algorithm</h3>

<pre>
1. Create an empty HashMap called seen.
2. Go through the array one number at a time.
3. Calculate:
       needed = target - current number
4. Check if needed is already in seen.
5. If yes, return the index of needed and the current index.
6. If no, store the current number and its index.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen:
                return [seen[needed], i]

            seen[nums[i]] = i
</pre>

<h3>Example</h3>

<pre>
nums = [2, 7, 11, 15]
target = 9

current = 2
needed = 9 - 2 = 7

7 is not in seen
→ store 2

seen = {2: 0}

current = 7
needed = 9 - 7 = 2

2 is already in seen
→ return [0, 1]
</pre>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The HashMap can store up to <code>n</code> elements.</p>

<h3>Pattern</h3>

<p><strong>HashMap / Dictionary</strong></p>
