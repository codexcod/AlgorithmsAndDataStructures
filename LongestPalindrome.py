import math


def expandFromMiddle(s, left, right):
    if s is None or left > right:
        return 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def findLongestPalindrome(string):
    start = 0
    end = 0

    for i in range(len(string)):
        len1 = expandFromMiddle(string, i, i)
        len2 = expandFromMiddle(string, i, i + 1)
        lenght = max(len1, len2)

        if lenght > end - start:
            start = i - (lenght - 1) // 2
            end = i + lenght // 2

    return string[start: end]
