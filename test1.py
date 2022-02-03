#!/usr/bin/env python3


def sub_number(n: int) -> int:
    """
    Subs numbers divisible by 3 with `Pick`, numbers divisible by 5 with `Aroo`
    and numbers divisible by both 3 and 5 with `Pickaroo`
    :return int:
    """

    if n % 5 == 0 == n % 3:
        return 'Pickaroo'

    if n % 5 == 0:
        return 'Aroo'

    if n % 3 == 0:
        return 'Pick'

    return n


if __name__ == '__main__':
    for i in range(1, 101):
        print(sub_number(i))
