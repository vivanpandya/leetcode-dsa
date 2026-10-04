<h2><a href="https://leetcode.com/problems/squares-of-a-sorted-array">Squares of a Sorted Array</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]

<strong>Explanation:</strong>
After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?</p>

<hr>

<h3>Approach</h3>

<p>We use the <strong>Two Pointer</strong> approach.</p>

<p>The array is already sorted, but after squaring the numbers, the order may change because negative numbers become positive.</p>

<p>The largest square will always come from either the <strong>leftmost</strong> number or the <strong>rightmost</strong> number.</p>

<p>We use two pointers:</p>

<ul>
	<li><code>left</code> points to the beginning of the array.</li>
	<li><code>right</code> points to the end of the array.</li>
</ul>

<p>We compare the absolute values of both numbers. The number with the larger absolute value will have the larger square.</p>

<p>We place the larger square at the end of the result array and move that pointer.</p>

<h3>Algorithm</h3>

<pre>
1. Create a result array of size n filled with 0.
2. Set left = 0.
3. Set right = n - 1.
4. Start filling result from the last position.
5. Compare abs(nums[left]) and abs(nums[right]).
6. Put the larger square into the current result position.
7. Move the corresponding pointer.
8. Continue until all positions are filled.
9. Return result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) &gt; abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result
</pre>

<h3>Example</h3>

<pre>
nums = [-4,-1,0,3,10]

left = 0
right = 4

Compare:
abs(-4) = 4
abs(10) = 10

10 is larger:
result[4] = 10² = 100
right = 3

Compare:
abs(-4) = 4
abs(3) = 3

4 is larger:
result[3] = (-4)² = 16
left = 1

Compare:
abs(-1) = 1
abs(3) = 3

3 is larger:
result[2] = 3² = 9
right = 2

Compare:
abs(-1) = 1
abs(0) = 0

1 is larger:
result[1] = (-1)² = 1
left = 2

Remaining:
0² = 0

Final result = [0,1,9,16,100]
</pre>

<h3>Why This Works</h3>

<p>Because the array is sorted, the largest absolute value must be at either end of the array.</p>

<p>For example:</p>

<pre>
[-4,-1,0,3,10]

Largest absolute value:
-4 → 4
10 → 10
</pre>

<p>So the largest square must be either <code>16</code> or <code>100</code>.</p>

<p>We always place the larger square at the end of the result array. By continuing this process, we fill the result from largest to smallest and finally get a sorted array.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — Each element is processed exactly once.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — We create a result array of size <code>n</code>.</p>

<h3>Pattern</h3>

<p><strong>Two Pointers / Sorted Array</strong></p>
