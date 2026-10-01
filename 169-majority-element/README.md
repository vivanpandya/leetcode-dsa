<h2><a href="https://leetcode.com/problems/majority-element">Majority Element</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that a majority element will exist in the array.</li>
</ul>

<p>&nbsp;</p>

<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

<hr>

<h3>Approach</h3>

<p>We use the <strong>Boyer-Moore Voting Algorithm</strong>.</p>

<p>We keep two variables:</p>

<ul>
	<li><code>candidate</code> → the current possible majority element.</li>
	<li><code>count</code> → keeps track of the candidate's count.</li>
</ul>

<p>For every number:</p>

<ol>
	<li>If <code>count</code> is <code>0</code>, make the current number the new <code>candidate</code>.</li>
	<li>If the current number is equal to <code>candidate</code>, increase <code>count</code>.</li>
	<li>If the current number is different, decrease <code>count</code>.</li>
</ol>

<p>The majority element appears more than half of the time, so it will remain as the final candidate.</p>

<h3>Algorithm</h3>

<pre>
1. Set candidate = 0.
2. Set count = 0.
3. Go through every number in the array.
4. If count == 0:
       Make the current number the candidate.
5. If current number == candidate:
       Increase count.
   Otherwise:
       Decrease count.
6. Return candidate.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def majorityElement(self, nums):
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
</pre>

<h3>Example</h3>

<pre>
nums = [2,2,1,1,1,2,2]

Start:
candidate = 0
count = 0

Number = 2
count = 0
candidate = 2
2 == 2
count = 1

Number = 2
2 == 2
count = 2

Number = 1
1 != 2
count = 1

Number = 1
1 != 2
count = 0

Number = 1
count = 0
candidate = 1
count = 1

Number = 2
2 != 1
count = 0

Number = 2
count = 0
candidate = 2
count = 1

Answer = 2
</pre>

<h3>Why This Works</h3>

<p>We can think of different numbers as cancelling each other.</p>

<p>For example:</p>

<pre>
majority element + different element = cancel
</pre>

<p>The majority element appears more than all other elements combined. Therefore, even after cancelling different elements, the majority element will remain as the final candidate.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use <code>candidate</code> and <code>count</code>.</p>

<h3>Pattern</h3>

<p><strong>Boyer-Moore Voting Algorithm</strong></p>
