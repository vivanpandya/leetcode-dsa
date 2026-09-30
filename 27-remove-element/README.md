<h2><a href="https://leetcode.com/problems/remove-element">Remove Element</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> from <code>nums</code> in-place.</p>

<p>Return the number of elements <code>k</code> which are not equal to <code>val</code>.</p>

<hr>

<h3>Approach</h3>

<p>We use one variable <code>index</code>.</p>

<p><code>index</code> tells us where the next valid number should be placed.</p>

<p>We go through every number:</p>

<ul>
    <li>If the number is equal to <code>val</code> → skip it.</li>
    <li>If the number is not equal to <code>val</code> → put it at <code>nums[index]</code> and move <code>index</code> forward.</li>
</ul>

<p>At the end, <code>index</code> is the number of elements which are not equal to <code>val</code>.</p>

<h3>Algorithm</h3>

<pre>
1. Set index = 0.
2. Go through every number in nums.
3. If nums[i] != val:
       Put nums[i] at nums[index].
       Increase index.
4. Return index.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def removeElement(self, nums, val):
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index
</pre>

<h3>Example</h3>

<pre>
nums = [3,2,2,3]
val = 3

index = 0

3 == 3
→ skip

2 != 3
→ nums[0] = 2
→ index = 1

2 != 3
→ nums[1] = 2
→ index = 2

3 == 3
→ skip

Final:
[2,2,_,_]

Return:
2
</pre>

<h3>Why This Works</h3>

<p>We only keep the numbers which are not equal to <code>val</code>.</p>

<p>We place every valid number at the front of the array.</p>

<p>The elements after <code>index</code> do not matter.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We check every element once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the same array and don't use another array.</p>

<h3>Pattern</h3>

<p><strong>Two Pointers / In-Place Array</strong></p>
