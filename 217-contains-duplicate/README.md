<h2><a href="https://leetcode.com/problems/contains-duplicate">Contains Duplicate</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The element 1 occurs at the indices 0 and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements are distinct.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,3,3,4,3,2,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use a <strong>HashSet (Set)</strong> to store the numbers we have already seen.</p>

<p>For every number:</p>

<ol>
	<li>Check if the number is already in the Set.</li>
	<li>If it is already present, it means we found a duplicate, so return <code>True</code>.</li>
	<li>If it is not present, add it to the Set.</li>
	<li>If we finish the whole array without finding a duplicate, return <code>False</code>.</li>
</ol>

<h3>Algorithm</h3>

<pre>
1. Create an empty Set called seen.
2. Go through the array one number at a time.
3. Check if the current number is already in seen.
4. If yes, return True.
5. If no, add the number to seen.
6. If the loop finishes, return False.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
</pre>

<h3>Example</h3>

<pre>
nums = [1, 2, 3, 1]

Start:
seen = {}

1 → not in seen → add 1
seen = {1}

2 → not in seen → add 2
seen = {1, 2}

3 → not in seen → add 3
seen = {1, 2, 3}

1 → already in seen
→ return True
</pre>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The Set can store up to <code>n</code> elements.</p>

<h3>Pattern</h3>

<p><strong>HashSet / Set</strong></p>
