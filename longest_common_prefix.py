# -*- coding: utf-8 -*-
"""longest common prefix

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EDuFCnwkcoyLZlxi7Zx8OITVrDtYUGnG
"""

#longest common prefix
def longestCommonPrefix(strs):
    n = len(strs)
    first = strs[0]
    len_first = len(first)
    for i in strs[1:]:
        while first != i[:len_first]:
            len_first -= 1
            if len_first == 0:
                return ""

            first = first[:len_first]

    return first

strs = ["dog","racecar","car"]
longestCommonPrefix(strs)