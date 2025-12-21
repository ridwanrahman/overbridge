# def main(haystack, needle):
    # first_occurrence = None
    # for i in range(len(haystack)):
    #     if i < len(needle):
    #         if haystack[i] == needle[i]:
    #             if first_occurrence is None:
    #                 first_occurrence = i
    #             continue
    #         else:
    #             first_occurrence = None
    #
    # if first_occurrence is None:
    #     return -1
    # return first_occurrence
def main(haystack, needle):
    needle_iter = 0
    needle_index = None
    for i in range(len(haystack)):
        if haystack[i] == needle[needle_iter]:
            if needle_index is None:
                full_word_haystack = haystack[i:i+len(needle)]
                if full_word_haystack == needle:
                    needle_index = i

    if needle_index is None:
        return -1
    return needle_index


if __name__ == "__main__":
    haystack = "mississippi"
    needle = "pi"
    haystack = "leetcode"
    needle = "leeto"
    haystack = "sadbutsad"
    needle = "sad"
    print(main(haystack, needle))
