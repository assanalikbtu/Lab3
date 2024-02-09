def is_prime(a):
    for i in range(2, a):
        if not a % i:
            return False
    return True


print(f'Prime numbers: {list(filter(lambda x: is_prime(x), [i for i in range(1, 101)]))}')