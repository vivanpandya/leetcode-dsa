<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays">Intersection of Two Arrays</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their <span data-keyword="array-intersection">intersection</span></em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use a <strong>Hash Set</strong> to find the common elements between the two arrays.</p>

<p>First, convert <code>nums1</code> into a set. This removes duplicate values automatically.</p>

<p>Then, go through <code>nums2</code> and check if each number exists in the set.</p>

<p>If it exists, add it to the result set. Since a set stores only unique values, duplicate elements will not be added again.</p>

<h3>Algorithm</h3>

<pre>
1. Convert nums1 into a set.
2. Create an empty result set.
3. Traverse every number in nums2.
4. If the number exists in the nums1 set:
       Add it to the result set.
5. Convert the result set into a list.
6. Return the list.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        result = set()

        for num in nums2:
            if num in seen:
                result.add(num)

        return list(result)
</pre>

<h3>Example</h3>

<pre>
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

Step 1:
seen = {4,9,5}

Step 2:

9 → exists → add 9
4 → exists → add 4
9 → already in result
8 → does not exist
4 → already in result

result = {9,4}

Answer = [9,4]
</pre>

<h3>Why This Works</h3>

<p>The set contains all unique elements from <code>nums1</code>.</p>

<p>When we check the elements of <code>nums2</code>, a number is added only if it also exists in <code>nums1</code>.</p>

<p>Because the result is also a set, every element appears only once.</p>

<p>Therefore, the result contains exactly the unique elements that are present in both arrays.</p>

<h3>Time Complexity</h3>

<p><strong>O(n + m)</strong> — We create a set from <code>nums1</code> and traverse <code>nums2</code> once.</p>

<h3>Space Complexity</h3>

<p><strong>O(n + m)</strong> — We use sets to store the elements of <code>nums1</code> and the result.</p>

<h3>Pattern</h3>

<p><strong>Hash Set / Set Intersection</strong></p>
