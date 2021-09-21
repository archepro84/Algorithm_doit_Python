from __future__ import annotations

from typing import Any


def gcd(x: int, y: int) -> int:
    """정숫값 x와 y의 최대 공약수를 반환"""
    print(x, y)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    print(gcd(22, 8))
