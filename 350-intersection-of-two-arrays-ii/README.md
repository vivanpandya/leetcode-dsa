<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii">Intersection of Two Arrays II</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must appear as many times as it shows in both arrays and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [4,9]
<strong>Explanation:</strong> [9,4] is also accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <code>nums1</code>&#39;s size is small compared to <code>nums2</code>&#39;s size? Which algorithm is better?</li>
	<li>What if elements of <code>nums2</code> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use a <strong>Hash Map (Dictionary)</strong> to store the frequency of each number in <code>nums1</code>.</p>

<p>For every number in <code>nums1</code>, we count how many times it appears.</p>

<p>Then, we traverse <code>nums2</code>. If a number exists in the dictionary and its count is greater than <code>0</code>, we add it to the result and decrease its count.</p>

<p>This makes sure that every number appears in the result only as many times as it appears in both arrays.</p>

<h3>Algorithm</h3>

<pre>
1. Create an empty dictionary called count.
2. Traverse nums1.
3. Store the frequency of every number in count.
4. Create an empty result list.
5. Traverse nums2.
6. If the current number exists in count and count[num] > 0:
       Add the number to result.
       Decrease count[num] by 1.
7. Return result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def intersect(self, nums1, nums2):
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        result = []

        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
</pre>

<h3>Example</h3>

<pre>
nums1 = [1,2,2,1]
nums2 = [2,2]

First, count nums1:

count = {
    1: 2,
    2: 2
}

Now check nums2:

2 → count[2] = 2
   Add 2
   count[2] = 1

2 → count[2] = 1
   Add 2
   count[2] = 0

Answer = [2,2]
</pre>

<h3>Why This Works</h3>

<p>The dictionary stores how many times each number appears in <code>nums1</code>.</p>

<p>When we find the same number in <code>nums2</code>, we add it to the result and decrease its count.</p>

<p>When the count becomes <code>0</code>, that number cannot be added again.</p>

<p>Therefore, each number appears in the result exactly as many times as it appears in both arrays.</p>

<h3>Time Complexity</h3>

<p><strong>O(n + m)</strong> — We traverse both arrays once.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The dictionary stores the frequency of elements from <code>nums1</code>.</p>

<h3>Pattern</h3>

<p><strong>Hash Map / Frequency Counting</strong></p>
