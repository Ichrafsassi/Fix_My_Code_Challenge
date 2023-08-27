#!/usr/bin/python3
""" FizzBuzz """
import sys


def fizzbuzz(n):
    """FizzBuzz function prints numbers from 1 to n separated by a space."""
    if n < 1:
        return

    res_tmp = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) != 0:
            res_tmp.append("Fizz")
        elif (i % 3) == 0 and (i % 5) == 0:
            res_tmp.append("FizzBuzz")
        elif (i % 5) == 0:
            res_tmp.append("Buzz")
        else:
            res_tmp.append(str(i))
    print(" ".join(res_tmp))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number 'n'")
        print("Usage: ./0-fizzbuzz.py <nr>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    n = int(sys.argv[1])
    fizzbuzz(n)