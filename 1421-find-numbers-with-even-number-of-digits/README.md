<h2><a href="https://leetcode.com/problems/find-numbers-with-even-number-of-digits">Find Numbers with Even Number of Digits</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>nums</code> of integers, return how many of them contain an <strong>even number</strong> of digits.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [12,345,2,6,7896]
<strong>Output:</strong> 2

<strong>Explanation:</strong>
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).

Therefore only 12 and 7896 contain an even number of digits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [555,901,482,1771]
<strong>Output:</strong> 1

<strong>Explanation:</strong>
Only 1771 contains an even number of digits.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We traverse every number in the array and count its digits.</p>

<p>To count the digits, we repeatedly divide the number by <code>10</code>. Every division removes one digit.</p>

<p>After counting the digits, we check whether the number of digits is even using:</p>

<pre>
digits % 2 == 0
</pre>

<p>If it is even, we increase the answer count.</p>

<h3>Algorithm</h3>

<pre>
1. Initialize count = 0.
2. Traverse every number in nums.
3. For each number:
       a. Initialize digits = 0.
       b. Repeatedly divide the number by 10.
       c. Increase digits by 1 after every division.
       d. Continue until the number becomes 0.
4. Check if digits is even.
5. If digits % 2 == 0:
       Increase count by 1.
6. Return count.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            digits = 0

            while num &gt; 0:
                num //= 10
                digits += 1

            if digits % 2 == 0:
                count += 1

        return count
</pre>

<h3>Example</h3>

<pre>
nums = [12,345,2,6,7896]

Start:
count = 0

12:
12 → 1 → 0
digits = 2
2 is even
count = 1

345:
345 → 34 → 3 → 0
digits = 3
3 is odd

2:
2 → 0
digits = 1
1 is odd

6:
6 → 0
digits = 1
1 is odd

7896:
7896 → 789 → 78 → 7 → 0
digits = 4
4 is even
count = 2

Answer = 2
</pre>

<h3>Why This Works</h3>

<p>Every time we divide a number by <code>10</code>, one digit is removed.</p>

<p>For example:</p>

<pre>
7896 → 789 → 78 → 7 → 0
</pre>

<p>We performed 4 divisions, so <code>7896</code> has 4 digits.</p>

<p>Since 4 is even, we increase the count.</p>

<p>We repeat this process for every number in the array, so the final count gives the number of elements with an even number of digits.</p>

<h3>Time Complexity</h3>

<p><strong>O(n × d)</strong> — We visit every number, and for each number we process its digits. Here, <code>d</code> is the number of digits.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use <code>count</code> and <code>digits</code> variables.</p>

<h3>Pattern</h3>

<p><strong>Array Traversal / Digit Counting</strong></p>
