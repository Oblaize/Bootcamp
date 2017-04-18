def prime_num_gen(n):

    if n < 0:
        return None
    elif n == 2:
        return [2]
    elif n == 1 or n == 0:
        return []

    if not isinstance(n, int):
        raise TypeError

    try:
        # initialize with 2 since its the smallest prime
        prime_nums = [2]
        for i in range(3, n + 1):
            # start from 3 onwards
            # "outer loop"
            factor_count = 0
            for x in range(2, i):
                # start from 2 onwards
                if i % x == 0:
                    factor_count += 1
                    # inner loop breaking..
                    break  # i is not a prime number
            if factor_count == 0:
                prime_nums.append(i)
    except TypeError as e:
        # n is not an integer
        raise (e)

    return prime_nums


if __name__ == '__main__':
    print prime_num_gen(9)