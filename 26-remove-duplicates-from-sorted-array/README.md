<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">Remove Duplicates from Sorted Array</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <strong>in-place</strong> so that each unique element appears only once.</p>

<p>Return the number of unique elements <code>k</code>.</p>

<hr>

<h3>Approach</h3>

<p>Because the array is already <strong>sorted</strong>, duplicate numbers are next to each other.</p>

<p>We use two pointers:</p>

<ul>
    <li><code>i</code> → position of the last unique number.</li>
    <li><code>j</code> → checks every number in the array.</li>
</ul>

<p>If <code>nums[j]</code> is different from <code>nums[i]</code>, we found a new unique number.</p>

<p>So we move <code>i</code> forward and put the new number there.</p>

<h3>Algorithm</h3>

<pre>
1. Set i = 0.
2. Start j from 1.
3. Compare nums[j] with nums[i].
4. If nums[j] != nums[i]:
       Move i forward.
       Put nums[j] at nums[i].
5. Continue until j reaches the end.
6. Return i + 1.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def removeDuplicates(self, nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
</pre>

<h3>Example</h3>

<pre>
nums = [0,0,1,1,1,2,2,3,3,4]

i = 0

j = 1
0 == 0
→ duplicate, skip

j = 2
1 != 0
→ i = 1
→ nums[1] = 1

Array:
[0,1,1,1,1,2,2,3,3,4]

j = 5
2 != 1
→ i = 2
→ nums[2] = 2

Array:
[0,1,2,1,1,2,2,3,3,4]

Continue...

Final first 5 elements:
[0,1,2,3,4]

Return 5
</pre>

<h3>Why This Works</h3>

<p>The array is sorted, so we only need to compare the current number with the last unique number.</p>

<p>Whenever we find a new number, we put it at the next available position.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We go through the array once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the same array and don't use another array.</p>

<h3>Pattern</h3>

<p><strong>Two Pointers / In-Place Array</strong></p>
