def reverse_integer(x: int) -> int:
    if x < 0:
        return -reverse_integer(-x)
    else:
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        return result

if __name__ == '__main__':
    print(reverse_integer(1230))
    print(reverse_integer(-1230))