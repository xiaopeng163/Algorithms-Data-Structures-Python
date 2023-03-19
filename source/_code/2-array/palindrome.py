def is_palindrome_pythonic(s):
    """Return True if the given string is a palindrome."""
    return s == s[::-1]


def is_palindrome(s):
    """Return True if the given string is a palindrome."""
    start_index = 0
    end_index = len(s) - 1
    while start_index < end_index:
        if s[start_index] != s[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


def leetcode_valid_palindrome(s: str) -> bool:

    # https://leetcode.com/problems/valid-palindrome/

    if len(s) == 0:
        return True
    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    s = "abba"
    print(is_palindrome(s))
    s = "1A man, a plan, a canal: Panama1"
    print(leetcode_valid_palindrome(s))
