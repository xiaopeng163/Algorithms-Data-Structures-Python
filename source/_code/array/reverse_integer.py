def reverse_integer(x: int) -> int:
    if x < 0:
        return -reverse_integer(-x)
    else:
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        return result


def reverse_integer2(x: int) -> int:
    if x < 0:  # for negative numbers, -100
        x = -x  # 100
        x = int(str(x)[::-1])  # '001' -> '1'
        x = -x  # -1
    else:  # for positive numbers, 100
        x = int(str(x)[::-1])
    if x < -(2**31) or x > 2**31 - 1:
        # if x is out of range,
        return 0
    return x


if __name__ == "__main__":
    print(reverse_integer(1230))
    print(reverse_integer(-1230))
    print(reverse_integer2(1230))
    print(reverse_integer2(-1230))
