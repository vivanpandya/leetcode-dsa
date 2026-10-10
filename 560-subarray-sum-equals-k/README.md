<h1>560. Subarray Sum Equals K</h1>

<p><strong>Difficulty:</strong> Medium</p>

<p><strong>Topics:</strong> Array, Hash Table, Prefix Sum</p>

<p><strong>LeetCode:</strong> <a href="https://leetcode.com/problems/subarray-sum-equals-k/">Subarray Sum Equals K</a></p>

<hr>

<h2>Problem Statement</h2>

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return the total number of subarrays whose sum equals <code>k</code>.</p>

<p>A subarray is a contiguous, non-empty sequence of elements within an array.</p>

<h3>Example 1</h3>

<pre>
Input: nums = [1,1,1], k = 2
Output: 2
</pre>

<h3>Example 2</h3>

<pre>
Input: nums = [1,2,3], k = 3
Output: 2
</pre>

<h3>Constraints</h3>

<ul>
<li><code>1 &lt;= nums.length &lt;= 2 * 10^4</code></li>
<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
<li><code>-10^7 &lt;= k &lt;= 10^7</code></li>
</ul>

<hr>

<h2>Approach</h2>

<p>We use the <strong>Prefix Sum + Hash Map</strong> technique to count subarrays efficiently.</p>

<p>A prefix sum is the sum of all elements processed from the beginning of the array up to the current position.</p>

<p>Let <code>prefix_sum</code> be the current prefix sum. If an earlier prefix sum equals <code>prefix_sum - k</code>, the elements between that earlier position and the current position have a sum of <code>k</code>.</p>

<p>We maintain a dictionary called <code>prefix_count</code> to store how many times each prefix sum has appeared.</p>

<ol>
<li>Initialize <code>count = 0</code> and <code>prefix_sum = 0</code>.</li>
<li>Initialize <code>prefix_count = {0: 1}</code> to account for subarrays starting at index zero.</li>
<li>Traverse the array and update the prefix sum.</li>
<li>Check how many times <code>prefix_sum - k</code> appears in the dictionary.</li>
<li>Add that frequency to the answer.</li>
<li>Record the current prefix sum in the dictionary.</li>
</ol>

<h2>Algorithm</h2>

<ol>
<li>Create a variable <code>count</code> initialized to zero.</li>
<li>Create a variable <code>prefix_sum</code> initialized to zero.</li>
<li>Create a dictionary <code>prefix_count = {0: 1}</code>.</li>
<li>For each number in <code>nums</code>:
    <ul>
    <li>Add the number to <code>prefix_sum</code>.</li>
    <li>Calculate <code>prefix_sum - k</code>.</li>
    <li>Add its frequency in <code>prefix_count</code> to <code>count</code>, using zero if the key is absent.</li>
    <li>Increment the frequency of the current <code>prefix_sum</code> in the dictionary.</li>
    </ul>
</li>
<li>Return <code>count</code>.</li>
</ol>

<h2>Code</h2>

<pre><code class="language-python">class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num

            count += prefix_count.get(prefix_sum - k, 0)

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count
</code></pre>

<h2>Example Walkthrough</h2>

<p><strong>Input:</strong></p>

<pre><code>nums = [1, 1, 1]
k = 2</code></pre>

<p><strong>Initial values:</strong></p>

<pre><code>count = 0
prefix_sum = 0
prefix_count = {0: 1}</code></pre>

<table>
<thead>
<tr><th>Step</th><th>num</th><th>prefix_sum</th><th>prefix_sum - k</th><th>count</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>1</td><td>1</td><td>-1</td><td>0</td></tr>
<tr><td>2</td><td>1</td><td>2</td><td>0</td><td>1</td></tr>
<tr><td>3</td><td>1</td><td>3</td><td>1</td><td>2</td></tr>
</tbody>
</table>

<p><strong>Explanation:</strong></p>

<ul>
<li>At step 1, no earlier prefix sum produces a subarray with sum 2.</li>
<li>At step 2, the earlier prefix sum 0 gives the subarray <code>[1,1]</code>.</li>
<li>At step 3, the earlier prefix sum 1 gives another subarray <code>[1,1]</code>.</li>
</ul>

<p><strong>Output:</strong> <code>2</code></p>

<h2>Why This Works</h2>

<p>For a current prefix sum <code>P</code>, a subarray has sum <code>k</code> whenever an earlier prefix sum equals <code>P - k</code>.</p>

<p>The dictionary records the frequency of every earlier prefix sum, allowing us to count all valid subarrays ending at the current position. We then record the current prefix sum for future elements.</p>

<p>Initializing <code>prefix_count</code> with <code>{0: 1}</code> ensures that subarrays beginning at index zero are counted correctly.</p>

<p>This method also handles negative numbers and zeros, unlike a standard sliding-window approach that relies on non-negative elements.</p>

<h2>Time Complexity</h2>

<p><strong>O(n)</strong> average, where <code>n</code> is the length of <code>nums</code>.</p>

<p>Each element is processed once, and dictionary lookups and updates take constant time on average.</p>

<h2>Space Complexity</h2>

<p><strong>O(n)</strong>, because the dictionary can store up to <code>n + 1</code> distinct prefix sums.</p>

<h2>Pattern</h2>

<p><strong>Primary Pattern:</strong> Prefix Sum</p>

<p><strong>Secondary Pattern:</strong> Hash Map / Frequency Counting</p>

<p><strong>When to use this pattern:</strong></p>

<ul>
<li>Counting subarrays whose sum equals a target.</li>
<li>Finding contiguous subarrays with a specific sum.</li>
<li>Handling arrays containing positive numbers, negative numbers, and zeros.</li>
<li>Counting how many times a cumulative sum has occurred.</li>
</ul>

<p><strong>Key takeaway:</strong> For a current prefix sum <code>P</code>, look for the earlier prefix sum <code>P - k</code>. Store prefix-sum frequencies in a hash map to count valid subarrays in linear time.</p>
