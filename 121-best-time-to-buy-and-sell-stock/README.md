<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">Best Time to Buy and Sell Stock</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We need to find the <strong>lowest buying price</strong> and then find the best selling price after it.</p>

<p>We keep two variables:</p>

<ul>
	<li><code>min_price</code> → lowest price we have seen so far.</li>
	<li><code>max_profit</code> → maximum profit found so far.</li>
</ul>

<p>For every price:</p>

<ol>
	<li>If the current price is smaller than <code>min_price</code>, update <code>min_price</code>.</li>
	<li>Calculate the profit if we sell today:</li>
</ol>

<pre>
profit = current price - min_price
</pre>

<ol start="3">
	<li>Update <code>max_profit</code> if the current profit is bigger.</li>
</ol>

<h3>Algorithm</h3>

<pre>
1. Set min_price = first price.
2. Set max_profit = 0.
3. Go through every price in the array.
4. If current price is smaller than min_price:
       update min_price.
5. Calculate:
       profit = current price - min_price
6. If profit is greater than max_profit:
       update max_profit.
7. Return max_profit.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price &lt; min_price:
                min_price = price

            profit = price - min_price

            if profit &gt; max_profit:
                max_profit = profit

        return max_profit
</pre>

<h3>Example</h3>

<pre>
prices = [7,1,5,3,6,4]

Start:
min_price = 7
max_profit = 0

Price = 7
profit = 7 - 7 = 0

Price = 1
1 is smaller than 7
min_price = 1

Price = 5
profit = 5 - 1 = 4
max_profit = 4

Price = 3
profit = 3 - 1 = 2

Price = 6
profit = 6 - 1 = 5
max_profit = 5

Price = 4
profit = 4 - 1 = 3

Answer = 5
</pre>

<h3>Why This Works</h3>

<p>We always keep the cheapest price we have seen before the current day.</p>

<p>So when we calculate:</p>

<pre>
profit = current price - min_price
</pre>

<p>we are always buying before selling.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We only use two variables.</p>

<h3>Pattern</h3>

<p><strong>Greedy / One Pass</strong></p>
