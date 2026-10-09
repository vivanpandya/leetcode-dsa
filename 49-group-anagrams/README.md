 <h2><a href="https://leetcode.com/problems/group-anagrams">Group Anagrams</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

<hr>

<p>Given an array of strings <code>strs</code>, group the anagrams together. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is no string in strs that can be rearranged to form <code>"bat"</code>.</li>
	<li>The strings <code>"nat"</code> and <code>"tan"</code> are anagrams as they can be rearranged to form each other.</li>
	<li>The strings <code>"ate"</code>, <code>"eat"</code>, and <code>"tea"</code> are anagrams as they can be rearranged to form each other.</li>
</ul>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

<hr>

<h3>Approach</h3>

<p>We use a <strong>Hash Map + Sorting</strong> approach.</p>

<p>Two strings are anagrams if they contain the same characters with the same frequencies, even if their characters appear in a different order.</p>

<p>For every word, we sort its characters alphabetically and use the sorted string as the dictionary key.</p>

<pre>
"eat" → "aet"
"tea" → "aet"
"ate" → "aet"
</pre>

<p>Since these words have the same sorted key, they are stored in the same group.</p>

<p>If the key does not exist, we create an empty list for it. Then we append the original word to that list.</p>

<h3>Algorithm</h3>

<pre>
1. Create an empty dictionary called groups.
2. Traverse every word in strs.
3. Sort the characters of the current word.
4. Join the sorted characters to create a key.
5. If the key is not in groups:
       Create an empty list for that key.
6. Append the original word to groups[key].
7. Return all dictionary values as a list.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
</pre>

<h3>Example</h3>

<pre>
strs = ["eat","tea","tan","ate","nat","bat"]

Step 1: Process "eat"
key = "aet"
groups = {"aet": ["eat"]}

Step 2: Process "tea"
key = "aet"
groups = {"aet": ["eat", "tea"]}

Step 3: Process "tan"
key = "ant"
groups = {
    "aet": ["eat", "tea"],
    "ant": ["tan"]
}

Step 4: Process "ate"
key = "aet"
groups["aet"] = ["eat", "tea", "ate"]

Step 5: Process "nat"
key = "ant"
groups["ant"] = ["tan", "nat"]

Step 6: Process "bat"
key = "abt"
groups["abt"] = ["bat"]

Final Answer:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
</pre>

<h3>Why This Works</h3>

<p>Sorting a string does not change its character frequencies. Therefore, anagrams always produce the same sorted string.</p>

<p>For example, <code>"eat"</code>, <code>"tea"</code>, and <code>"ate"</code> all produce the key <code>"aet"</code>.</p>

<p>Non-anagrams produce different sorted keys, so they are placed in different groups.</p>

<p>Using the sorted string as a dictionary key allows us to group all anagrams correctly.</p>

<h3>Time Complexity</h3>

<p><strong>O(n × m log m)</strong> — Let <code>n</code> be the number of strings and <code>m</code> the maximum length of a string. Sorting each string takes <code>O(m log m)</code>, and we do this for every string.</p>

<h3>Space Complexity</h3>

<p><strong>O(n × m)</strong> — The dictionary stores all original strings and their sorted keys. This describes the input-dependent storage used by the solution.</p>

<h3>Pattern</h3>

<p><strong>Hash Map + Sorting / Grouping by Key</strong></p>
