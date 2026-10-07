<h2><a href="https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side">Replace Elements with Greatest Element on Right Side</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given an array <code>arr</code>, replace every element in that array with the greatest element among the elements to its right, and replace the last element with <code>-1</code>.</p>

<p>After doing so, return the array.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [17,18,5,4,6,1]
<strong>Output:</strong> [18,6,6,6,1,-1]
<strong>Explanation:</strong>
- index 0 --&gt; the greatest element to the right of index 0 is index 1 (18).
- index 1 --&gt; the greatest element to the right of index 1 is index 4 (6).
- index 2 --&gt; the greatest element to the right of index 2 is index 4 (6).
- index 3 --&gt; the greatest element to the right of index 3 is index 4 (6).
- index 4 --&gt; the greatest element to the right of index 4 is index 5 (1).
- index 5 --&gt; there are no elements to the right of index 5, so we put -1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [400]
<strong>Output:</strong> [-1]
<strong>Explanation:</strong> There are no elements to the right of index 0.
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<hr>

<h3>Approach</h3>

<p>We traverse the array from <strong>right to left</strong> and keep track of the greatest element seen so far.</p>

<p>We use a variable <code>max_right</code> to store the greatest element to the right of the current position.</p>

<p>For every element:</p>

<ol>
	<li>Store the current element in a temporary variable.</li>
	<li>Replace the current element with <code>max_right</code>.</li>
	<li>Update <code>max_right</code> using the original current element.</li>
</ol>

<p>For the last element, <code>max_right</code> starts as <code>-1</code>, so it is automatically replaced with <code>-1</code>.</p>

<h3>Algorithm</h3>

<pre>
1. Initialize max_right = -1.
2. Traverse arr from right to left.
3. Store the current element in a variable current.
4. Replace arr[i] with max_right.
5. Update max_right:

       max_right = max(max_right, current)

6. Return the modified array.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def replaceElements(self, arr):
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]

            arr[i] = max_right

            max_right = max(max_right, current)

        return arr
</pre>

<h3>Example</h3>

<pre>
arr = [17,18,5,4,6,1]

Start:
max_right = -1

i = 5:
current = 1
arr[5] = -1
max_right = 1

i = 4:
current = 6
arr[4] = 1
max_right = 6

i = 3:
current = 4
arr[3] = 6
max_right = 6

i = 2:
current = 5
arr[2] = 6
max_right = 6

i = 1:
current = 18
arr[1] = 6
max_right = 18

i = 0:
current = 17
arr[0] = 18
max_right = 18

Answer = [18,6,6,6,1,-1]
</pre>

<h3>Why This Works</h3>

<p>When we traverse from right to left, all elements to the right of the current position have already been processed.</p>

<p>Therefore, <code>max_right</code> always contains the greatest element to the right of the current index.</p>

<p>For example, when processing <code>5</code>:</p>

<pre>
Elements to the right = [4,6,1]

max_right = 6
</pre>

<p>So we replace <code>5</code> with <code>6</code>.</p>

<p>Because we process every element from right to left, we can solve the problem in a single traversal.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse the array exactly once.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> — We modify the array in-place and use only a few variables.</p>

<h3>Pattern</h3>

<p><strong>Right-to-Left Traversal / Running Maximum</strong></p>
