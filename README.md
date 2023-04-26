# Longest-Common-Mountain-Subsequence
Calculates the longest common elements from arrays which are also like a mountain

Given two sequences A = {a1, a2, …, a|A|} and B = {b1, b2, …, b|B|}, a sequence C = {c1, c2, …, c|C|}
is called a common mountain subsequence of A and B, if (i) there exist two strictly increasing
functions f and g (meaning f(x1) < f(x2) if x1 < x2), such that ci = af(i) = bg(i) for all 1 ≤ i ≤ |C|; and
(ii) there exists an index k, such that c1 < c2 < … < ck > ck+1 > … > c|C|, for some k in 1 ≤ k ≤ |C|.
In simple words, the sequence C must be a subsequence of A and a subsequence of B at the same
time (not necessarily continuous, e.g., it is possible that c1 = a1, c2 = a3, c3 = a6, …), and C has a
peak, from which values decrease towards both left side and right side. There are many such
common mountain subsequences between A and B, however, there is a longest subsequence among
them. In this question, you are to write a program which computes the length of a longest common
mountain subsequence.

Why this exercise?
1. Very common leetcode question but this is another good variation to the typical LCMS problem 
