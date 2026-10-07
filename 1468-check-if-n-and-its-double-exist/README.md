<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">Check If N and Its Double Exist</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>arr</code> of integers, check if there exist two indices <code>i</code> and <code>j</code> such that:</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use a <strong>Hash Set</strong> to store the numbers that we have already seen.</p>

<p>For every number <code>num</code>, we check two possibilities:</p>

<pre>
2 * num
num / 2
</pre>

<p>If either value already exists in the set, we have found two different elements satisfying the condition.</p>

<p>We also check <code>num % 2 == 0</code> before checking <code>num // 2</code>, because only even numbers have an integer half.</p>

<h3>Algorithm</h3>

<pre>
1. Create an empty Hash Set called seen.
2. Traverse every number num in arr.
3. Check if 2 * num is already present in seen.
4. If num is even, check if num // 2 is already present in seen.
5. If either condition is true, return True.
6. Add num to seen.
7. If no valid pair is found, return False.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def checkIfExist(self, arr):
        seen = set()

        for num in arr:
            if 2 * num in seen:
                return True

            if num % 2 == 0 and num // 2 in seen:
                return True

            seen.add(num)

        return False
</pre>

<h3>Example</h3>

<pre>
arr = [10,2,5,3]

Start:
seen = {}

num = 10:
2 * 10 = 20 → not in seen
10 // 2 = 5 → not in seen
Add 10

seen = {10}

num = 2:
2 * 2 = 4 → not in seen
2 // 2 = 1 → not in seen
Add 2

seen = {10,2}

num = 5:
2 * 5 = 10 → already in seen

Therefore:
Answer = True
</pre>

<h3>Why This Works</h3>

<p>For every number, we check whether its double or its half has already appeared in the array.</p>

<p>For example, when we reach <code>5</code>:</p>

<pre>
2 * 5 = 10
</pre>

<p>Since <code>10</code> is already in the Hash Set, the pair <code>(10, 5)</code> satisfies:</p>

<pre>
10 = 2 * 5
</pre>

<p>Therefore, we return <code>True</code>.</p>

<p>If we finish traversing the array without finding such a pair, we return <code>False</code>.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array once, and Hash Set lookups take <code>O(1)</code> average time.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The Hash Set can store up to <code>n</code> elements.</p>

<h3>Pattern</h3>

<p><strong>Hash Set / Fast Lookup</strong></p>
