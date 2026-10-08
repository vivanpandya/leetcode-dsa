<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">Top K Frequent Elements</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2,1,2,3,1,3,2], k = 2
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong> Your algorithm's time complexity must be better than <code>O(n log n)</code>, where n is the array's size.</p>

<hr>

<h3>Approach</h3>

<p>We use <strong>Hash Map + Bucket Sort</strong> to solve this problem in <strong>O(n)</strong> time.</p>

<p>First, we use a dictionary to count how many times each number appears in the array.</p>

<p>For example:</p>

<pre>
nums = [1,1,1,2,2,3]

Frequency:
1 → 3
2 → 2
3 → 1
</pre>

<p>Then we create buckets where the <strong>index represents the frequency</strong>.</p>

<pre>
bucket[1] = [3]
bucket[2] = [2]
bucket[3] = [1]
</pre>

<p>Finally, we traverse the buckets from the highest frequency to the lowest frequency and add elements to the result until we have <code>k</code> elements.</p>

<h3>Algorithm</h3>

<pre>
1. Create an empty Hash Map called count.
2. Traverse nums and count the frequency of every number.
3. Create n + 1 empty buckets.
4. For every number and its frequency:
       Add the number to the bucket at that frequency.
5. Traverse the buckets from highest frequency to lowest frequency.
6. Add each element to the result.
7. Stop when the result contains k elements.
8. Return the result.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frq in count.items():
            buckets[frq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
</pre>

<h3>Example</h3>

<pre>
nums = [1,1,1,2,2,3]
k = 2

Step 1: Count frequencies

count = {
    1: 3,
    2: 2,
    3: 1
}

Step 2: Create buckets

bucket[3] = [1]
bucket[2] = [2]
bucket[1] = [3]

Step 3: Traverse from highest frequency

Frequency 3:
result = [1]

Frequency 2:
result = [1,2]

Now len(result) == k.

Answer = [1,2]
</pre>

<h3>Why This Works</h3>

<p>The frequency map tells us exactly how many times each number appears.</p>

<p>We then place every number into a bucket based on its frequency. Since a number can appear at most <code>n</code> times, we only need <code>n + 1</code> buckets.</p>

<p>By traversing the buckets from the highest frequency to the lowest frequency, we encounter the most frequent elements first.</p>

<p>We stop as soon as we collect <code>k</code> elements, so the result contains exactly the <code>k</code> most frequent elements.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We count frequencies, create the buckets, and traverse the buckets. Each operation is linear in the size of the input.</p>

<h3>Space Complexity</h3>

<p><strong>O(n)</strong> — The frequency map and buckets can store up to <code>n</code> elements.</p>

<h3>Pattern</h3>

<p><strong>Hash Map + Bucket Sort / Frequency Counting</strong></p>
