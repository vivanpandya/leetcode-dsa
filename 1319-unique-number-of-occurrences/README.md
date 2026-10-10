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
<li>Initialize an empty dictionary called <code>count</code>.</li>
<li>Iterate through <code>arr</code> and increment the frequency of each number.</li>
<li>Create a list called <code>frequencies</code> containing the dictionary's values.</li>
<li>Convert <code>frequencies</code> into a set.</li>
<li>Return whether the lengths of the list and set are equal.</li>
</ol>

<h2>Code</h2>

<pre><code class="language-python">class Solution:
    def uniqueOccurrences(self, arr):
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        frequencies = list(count.values())

        return len(frequencies) == len(set(frequencies))
</code></pre>

<h2>Example Walkthrough</h2>

<p><strong>Input:</strong></p>

<pre><code>arr = [1, 2, 2, 1, 1, 3]</code></pre>

<p><strong>Step 1: Count the occurrences.</strong></p>

<pre><code>{
    1: 3,
    2: 2,
    3: 1
}</code></pre>

<p><strong>Step 2: Extract the frequencies.</strong></p>

<pre><code>frequencies = [3, 2, 1]</code></pre>

<p><strong>Step 3: Convert the frequencies into a set.</strong></p>

<pre><code>set(frequencies) = {1, 2, 3}</code></pre>

<p><strong>Step 4: Compare their lengths.</strong></p>

<pre><code>len(frequencies) == len(set(frequencies))
3 == 3
</code></pre>

<p><strong>Output:</strong> <code>True</code></p>

<h2>Why This Works</h2>

<p>The dictionary stores the occurrence count of every distinct number. The set removes duplicate frequency values.</p>

<p>If the list and set have equal lengths, every frequency is unique. If their lengths differ, at least two numbers share the same occurrence count.</p>

<h2>Time Complexity</h2>

<p><strong>O(n)</strong> average, where <code>n</code> is the length of the array.</p>

<p>We traverse the array once to count occurrences. Creating the frequency list and set takes linear time in the number of distinct values.</p>

<h2>Space Complexity</h2>

<p><strong>O(n)</strong>, where <code>n</code> is the length of the array.</p>

<p>The dictionary, frequency list, and set can each store up to the number of distinct values in the array.</p>

<h2>Pattern</h2>

<p><strong>Primary Pattern:</strong> Hash Map / Frequency Counting</p>

<p><strong>Secondary Pattern:</strong> Hash Set / Uniqueness Checking</p>

<p><strong>When to use this pattern:</strong></p>

<ul>
<li>Counting the frequency of array elements.</li>
<li>Checking whether all frequencies are distinct.</li>
<li>Detecting duplicate frequency values.</li>
<li>Solving problems involving frequency comparisons.</li>
</ul>

<p><strong>Key takeaway:</strong> Count each element with a dictionary, then use a set to check whether all occurrence counts are unique.</p>
