<h1>1207. Unique Number of Occurrences</h1>

<p><strong>Difficulty:</strong> Easy</p>

<p><strong>Topics:</strong> Array, Hash Table, Hash Set</p>

<p><strong>LeetCode:</strong> <a href="https://leetcode.com/problems/unique-number-of-occurrences/">Unique Number of Occurrences</a></p>

<hr>

<h2>Problem Statement</h2>

<p>Given an array of integers <code>arr</code>, return <code>true</code> if the number of occurrences of each value in the array is unique, or <code>false</code> otherwise.</p>

<h3>Example 1</h3>

<pre>
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2, and 3 has 1.
No two values have the same number of occurrences.
</pre>

<h3>Example 2</h3>

<pre>
Input: arr = [1,2]
Output: false
</pre>

<h3>Example 3</h3>

<pre>
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
</pre>

<h3>Constraints</h3>

<ul>
<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
<li><code>-1000 &lt;= arr[i] &lt;= 1000</code></li>
</ul>

<hr>

<h2>Approach</h2>

<p>We use a <strong>Hash Map + Hash Set</strong> approach.</p>

<ol>
<li>Use a dictionary to count the frequency of each number.</li>
<li>Extract all frequency values from the dictionary.</li>
<li>Convert the frequencies into a set, which automatically removes duplicate values.</li>
<li>Compare the number of frequencies with the number of unique frequencies.</li>
<li>If both lengths are equal, return <code>True</code>; otherwise, return <code>False</code>.</li>
</ol>

<h2>Algorithm</h2>

<ol>
<li
