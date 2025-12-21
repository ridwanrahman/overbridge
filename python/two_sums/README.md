There are 2 ways to solve this problem.

Brute Force

This can be done by using two loops and then finding the difference till the target is found.
This is a terrible approach as the time complexity is O(n^2).


Using a dict

This is the best approach. In a dict, append each num as the key
before adding each, check whether it meets the target. If the difference exists in the dict, then return it. Otherwise keep adding into the dict