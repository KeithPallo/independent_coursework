def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not

    A triangular number is a number obtained by the continued summation of integers starting from 1.
    For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
    """

    sum = 0
    start = 0

    # The formula for a triangular number is T = (n)(n + 1) / 2.
    # This is applied in a while loop method below

    while sum <= k:
        start += 1
        sum = sum + start
        if sum == k:
            return True
            break

    return False
