def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)

    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def eval(x):
        y = 0 # Initialize a 0 value

        # Multiply the previous ith in the list term by y (adding one to each exponent for all terms that went
        # through the loop, and add the current term as a constant

        for num in L:
            y = y*x + num
        return y

    return eval