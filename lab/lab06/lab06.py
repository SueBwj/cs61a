this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def add_helper(b):
        nonlocal a
        a = a + 1
        return a + b - 1
    return add_helper


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    a0 = 0
    a1 = 1
    n = -1

    def fib():
        # 用a0 和 a1 存储状态的值， n表示第几个
        nonlocal a0
        nonlocal a1
        nonlocal n
        n += 1
        if (n == 0):
            return 0
        else:
            if (n % 2 == 1):
                a1 = a1 + a0
                return a1
            else:
                a0 = a0 + a1
                return a0
    return fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    # be careful of the situation that entry and elem are equivalent.
    # so as not to create an infinitely long list while iterating through it
    i = 0
    while (i < len(lst)):
        if (lst[i] == entry):
            lst.insert(i+1, elem)
            if entry == elem:
                i += 2
        i += 1
    return lst
