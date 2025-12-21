# Initialize an empty string ans to store the common prefix.
# Sort the input list v lexicographically. This step is necessary because the common prefix should be common to all the strings, so we need to find the common prefix of the first and last string in the sorted list.
# Iterate through the characters of the first and last string in the sorted list, stopping at the length of the shorter string.
# If the current character of the first string is not equal to the current character of the last string, return the common prefix found so far.
# Otherwise, append the current character to the ans string.
# Return the ans string containing the longest common prefix.

from typing import List


def main(v: List):
    ans=""
    v=sorted(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans

if __name__ == "__main__":
    data = ["flower", "flow", "flight"]
    print(main(data))
