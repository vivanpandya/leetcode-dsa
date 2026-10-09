 <h2><a href="https://leetcode.com/problems/valid-anagram">Valid Anagram</a></h2>

<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

<hr>

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

<hr>

<h3>Approach</h3>

<p>We use a <strong>Hash Map + Character Frequency Counting</strong> approach to solve the problem in <code>O(n)</code> time.</p>

<p>Two strings are anagrams if they contain exactly the same characters with the same frequencies, regardless of their order.</p>

<p>First, we check whether the lengths of <code>s</code> and <code>t</code> are equal. If they are different, they cannot be anagrams.</p>

<p>Next, we count the frequency of each character in <code>s</code> using a dictionary. Then, we traverse <code>t</code> and decrease the corresponding character counts.</p>

<p>If a character does not exist in the dictionary or its count is already zero, we return <code>False</code>. Otherwise, after processing every character, we return <code>True</code>.</p>

<h3>Algorithm</h3>

<pre>
1. If the lengths of s and t are different, return False.
2. Create an empty dictionary called count.
3. Traverse every character in s.
4. Increase the frequency of each character in count.
5. Traverse every character in t.
6. If the character is missing from count or its frequency is zero:
       Return False.
7. Otherwise, decrease its frequency by 1.
8. Return True if all characters are processed successfully.
</pre>

<h3>Code</h3>

<pre>
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return False

            count[ch] -= 1

        return True
</pre>

<h3>Example</h3>

<pre>
s = "anagram"
t = "nagaram"

Step 1: Count characters in s

a → 3
n → 1
g → 1
r → 1
m → 1

Step 2: Process characters in t

n → 1 - 1 = 0
a → 3 - 1 = 2
g → 1 - 1 = 0
a → 2 - 1 = 1
r → 1 - 1 = 0
a → 1 - 1 = 0
m → 1 - 1 = 0

All characters are matched successfully.

Answer = True
</pre>

<h3>Why This Works</h3>

<p>Anagrams must contain the same characters with identical frequencies.</p>

<p>The dictionary stores the frequency of each character in <code>s</code>. Every character found in <code>t</code> reduces its corresponding frequency by one.</p>

<p>If a character is missing or its frequency is zero before processing it, then <code>t</code> contains a character that cannot be matched with the remaining characters in <code>s</code>.</p>

<p>If every character is processed successfully and the strings have equal lengths, both strings contain exactly the same characters with the same frequencies.</p>

<h3>Time Complexity</h3>

<p><strong>O(n)</strong> — We traverse both strings once. Dictionary lookups and updates take <code>O(1)</code> average time.</p>

<h3>Space Complexity</h3>

<p><strong>O(1)</strong> auxiliary space for lowercase English letters, because there are only 26 possible characters. More generally, for <code>k</code> distinct characters, the dictionary requires <code>O(k)</code> space.</p>

<h3>Pattern</h3>

<p><strong>Hash Map + Character Frequency Counting</strong></p>
