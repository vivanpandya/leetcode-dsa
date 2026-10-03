<h2><a href="https://leetcode.com/problems/richest-customer-wealth">Richest Customer Wealth</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>You are given an <code>m x n</code> integer grid <code>accounts</code> where <code>accounts[i][j]</code> is the amount of money the <code>i<sup>th</sup></code> customer has in the <code>j<sup>th</sup></code> bank. Return <em>the <strong>wealth</strong> that the richest customer has.</em></p>

<p>A customer's <strong>wealth</strong> is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum <strong>wealth</strong>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[1,2,3],[3,2,1]]
<strong>Output:</strong> 6

<strong>Explanation:</strong>
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6

Both customers are considered the richest with a wealth of 6 each, so return 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[1,5],[7,3],[3,5]]
<strong>Output:</strong> 10

<strong>Explanation:</strong>
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8

The 2nd customer is the richest with a wealth of 10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[2,8,7],[7,1,3],[1,9,5]]
<strong>Output:</strong> 17
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == accounts.length</code></li>
	<li><code>n == accounts[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= accounts[i][j] &lt;= 100</code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>Each row in <code>accounts</code> represents one customer.</p>

<p>We calculate the sum of each customer's bank accounts to find their total wealth.</p>

<p>Then, we keep track of the maximum wealth found so far.</p>

<p>For each customer:</p>

<pre>
wealth = sum(customer)
</pre>

<p>If this wealth is greater than the current maximum, we update <code>max_wealth</code>.</p>

<h3>Algorithm</h3>

<pre>
1. Initialize max_wealth = 0.
2. Traverse each customer in accounts.
3. Calculate the sum of the customer's accounts.
4. Compare the current wealth with max_wealth.
5. If the current wealth is greater:
       Update max_wealth.
6. Return max_wealth.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)

            if wealth &gt; max_wealth:
                max_wealth = wealth

        return max_wealth
</pre>

<h3>Example</h3>

<pre>
accounts = [[1,5],[7,3],[3,5]]

Start:
max_wealth = 0

1st customer:
wealth = 1 + 5
       = 6

max_wealth = 6

2nd customer:
wealth = 7 + 3
       = 10

10 &gt; 6
max_wealth = 10

3rd customer:
wealth = 3 + 5
       = 8

8 &lt; 10
max_wealth = 10

Answer = 10
</pre>

<h3>Why This Works</h3>

<p>Each customer's wealth is the sum of all the money in their bank accounts.</p>

<p>By calculating the sum of every row, we get the wealth of every customer.</p>

<p>We keep the largest sum in <code>max_wealth</code>, so after checking all customers, it contains the wealth of the richest customer.</p>

<h3>Time Complexity</h3>

<p><strong>O(m × n)</strong> — We visit every account exactly once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use <code>max_wealth</code> and <code>wealth</code> and do not create any extra data structure.</p>

<h3>Pattern</h3>

<p><strong>2D Array / Matrix Traversal / Row Sum</strong></p>
