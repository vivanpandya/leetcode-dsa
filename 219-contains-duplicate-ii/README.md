<h2><a href="https://leetcode.com/problems/contains-duplicate-ii">Contains Duplicate II</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use a <strong>Hash Map</strong> to store the <strong>last index</strong> where each number appeared.</p>

<p>While traversing the array, if the current number has appeared before, we calculate the distance between the current index and its previous index.</p>

<pre>
current_index - previous_index
</pre>

<p>If this distance is less than or equal to <code>k</code>, we have found a valid duplicate and return <code>true</code>.</p>

<p>After checking, we update the number's index in the Hash Map with the current index.</p>

<h3>Algorithm</h3>

<pre>
1. Create an empty Hash Map called seen.
2. Traverse nums using index i.
3. If nums[i] is already present in seen:
       Calculate i - seen[nums[i]].
4. If the distance is <= k:
       Return true.
5. Update the latest index of nums[i].
6. If no valid duplicate is found, return false.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] &lt;= k:
                return True

            seen[nums[i]] = i

        return False
</pre>

<h3>Example</h3>

<pre>
nums = [1,2,3,1]
k = 3

Start:
seen = {}

i = 0:
num = 1
1 is not in seen
seen = {1: 0}

i = 1:
num = 2
2 is not in seen
seen = {1: 0, 2: 1}

i = 2:
num = 3
3 is not in seen
seen = {1: 0, 2: 1, 3: 2}

i = 3:
num = 1
1 is already in seen
previous index = 0

Distance:
3 - 0 = 3

Since 3 <= k:

Answer = true
</pre>

<h3>Why This Works</h3>

<p>The Hash Map stores the most recent index of every number.</p>

<p>When we see the same number again, we only need to compare the current index with its latest previous index.</p>

<p>The latest previous occurrence gives the smallest possible distance to the current occurrence. Therefore, if even this distance is greater than <code>k</code>, no earlier occurrence can satisfy the condition either.</p>

<p>For example:</p>

<pre>
nums = [1,2,3,1]
       ↑     ↑
       0     3

distance = 3 - 0 = 3
</pre>

<p>Since <code>3 &lt;= k</code>, the answer is <code>true</code>.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array once, and Hash Map lookup takes <code>O(1)</code> average time.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The Hash Map can store up to <code>n</code> different elements.</p>

<h3>Pattern</h3>

<p><strong>Hash Map / Last Index Tracking</strong></p>
