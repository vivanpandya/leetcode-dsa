<h2><a href="https://leetcode.com/problems/plus-one">Plus One</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>'s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>'s.</li>
</ul>

<hr>

<h3>Approach</h3>

<p>We start from the <strong>last digit</strong> because we need to add <code>1</code> from the right side.</p>

<p>There are two cases:</p>

<ul>
	<li>If the digit is less than <code>9</code>, simply add <code>1</code> and return.</li>
	<li>If the digit is <code>9</code>, change it to <code>0</code> and move to the previous digit.</li>
</ul>

<p>If all digits are <code>9</code>, we add <code>1</code> at the beginning.</p>

<h3>Algorithm</h3>

<pre>
1. Start from the last digit.
2. Check if the digit is less than 9.
3. If yes:
       Add 1 to it.
       Return the array.
4. If the digit is 9:
       Change it to 0.
       Move to the previous digit.
5. If all digits were 9:
       Add 1 at the beginning.
6. Return the array.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] != 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits
</pre>

<h3>Example</h3>

<pre>
digits = [1,2,9]

Start from the last digit:

9 → change to 0
[1,2,0]

Move to the previous digit:

2 → 2 + 1 = 3
[1,3,0]

Answer = [1,3,0]
</pre>

<p>For an array containing only 9's:</p>

<pre>
digits = [9,9,9]

9 → 0
9 → 0
9 → 0

[0,0,0]

Add 1 at the beginning:

[1,0,0,0]
</pre>

<h3>Why This Works</h3>

<p>We start from the right because adding 1 affects the last digit first.</p>

<p>If the digit is <code>9</code>, it becomes <code>0</code> and the extra <code>1</code> moves to the left.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — In the worst case, we may check every digit.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the given array directly. Only the all-9 case creates a new array.</p>

<h3>Pattern</h3>

<p><strong>Array + Carry</strong></p>
