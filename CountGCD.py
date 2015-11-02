"""
Problem: Count number of subsets of a set with GCD equal to a given number.

Description: Given a set of positive integer elements, find count of subsets with GCDs equal to
given numbers.

Examples:
1. Input:  arr[] = {2, 3, 4}, gcd[] = {2, 3}
   Output: Number of subsets with gcd 2 is 2
           Number of subsets with gcd 3 is 1
           The two subsets with GCD equal to 2 are {2} and {2, 4}.
           The one subset with GCD equal to 3 ss {3}.
2. Input:  arr[] = {6, 3, 9, 2}, gcd = {3, 2}
   Output: Number of subsets with gcd 3 is 5
           Number of subsets with gcd 2 is 2
           The five subsets with GCD equal to 3 are {3}, {6, 3}, {3, 9}, {6, 9) and {6, 3, 9}.
           The two subsets with GCD equal to 2 are {2} and {2, 6}.
http://www.geeksforgeeks.org/count-number-of-subsets-of-a-set-with-gcd-equal-to-a-given-number/
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__
