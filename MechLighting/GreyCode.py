def gray_decode(n):
    m = n >> 1
    while m:
        n ^= m
        m >>= 1
    return n