<h2><a href="https://leetcode.com/problems/merge-sorted-array">Merge Sorted Array</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in <strong>non-decreasing order</strong>.</p>

<p>Merge both arrays into <code>nums1</code> in sorted order.</p>

<hr>

<h3>Approach</h3>

<p>We use <strong>3 pointers</strong>:</p>

<ul>
    <li><code>i</code> → last actual element of <code>nums1</code></li>
    <li><code>j</code> → last element of <code>nums2</code></li>
    <li><code>k</code> → last position of <code>nums1</code></li>
</ul>

<p>We start merging from the <strong>end</strong>.</p>

<p>Why from the end?</p>

<p>Because <code>nums1</code> already has empty spaces at the end. If we start from the front, we may overwrite the existing elements of <code>nums1</code>.</p>

<p>So we compare the biggest elements of both arrays and put the bigger one at <code>nums1[k]</code>.</p>

<h3>Algorithm</h3>

<pre>
1. Set i = m - 1
2. Set j = n - 1
3. Set k = m + n - 1

4. While i >= 0 and j >= 0:
       Compare nums1[i] and nums2[j]

       If nums1[i] is bigger:
           nums1[k] = nums1[i]
           i -= 1

       Otherwise:
           nums1[k] = nums2[j]
           j -= 1

       k -= 1

5. If nums2 still has elements:
       Copy them into nums1.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] &gt; nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
</pre>

<h3>Example</h3>

<pre>
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

i = 2 → 3
j = 2 → 6
k = 5

3 vs 6
→ 6 is bigger
→ nums1[5] = 6

[1,2,3,0,0,6]

3 vs 5
→ 5 is bigger
→ nums1[4] = 5

[1,2,3,0,5,6]

3 vs 2
→ 3 is bigger
→ nums1[3] = 3

[1,2,3,3,5,6]

2 vs 2
→ nums2 value goes to nums1[2]

Final:
[1,2,2,3,5,6]
</pre>

<h3>Why This Works</h3>

<p>Both arrays are already sorted.</p>

<p>So the largest element will always be at the end of either array.</p>

<p>We compare those two largest elements and put the larger one at the end of <code>nums1</code>.</p>

<h3>Time Complexity</h3>

<p><strong>O(m + n)</strong> — We go through both arrays only once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify <code>nums1</code> directly and don't use another array.</p>

<h3>Pattern</h3>

<p><strong>Two Pointers / In-Place Merge</strong></p>
