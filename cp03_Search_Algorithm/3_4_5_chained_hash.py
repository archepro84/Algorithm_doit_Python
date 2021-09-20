from __future__ import annotations
from typing import Any, Type, Sequence
import hashlib


# 체인법으로 해시 함수 구현하기

class Node:
    """해시를 구성하는 노드 / """

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """Init"""
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """Hash Class"""

    def __init__(self, capacity: int) -> None:
        "Init"
        self.capacity = capacity  # Hash Table의 크기 지정
        self.table = [None] * self.capacity  # Hash Table(List)을 선언

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity


def seq_search(a: Sequence, key: Any) -> int:
    pass


if __name__ == '__main__':
    print(seq_search([1, 6, 2, 5, 3, 4, 7, 8], 99))
