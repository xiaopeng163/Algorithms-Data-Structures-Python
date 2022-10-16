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

if __name__ == "__main__":
    s = "abba"
    print(is_palindrome(s))
