from __future__ import annotations

import hashlib
from typing import Any
from enum import Enum


# OpenAddressing으로 해시 함수 구현하기


class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1  # 비어 있음
    DELETED = 2  # 삭제됨


class Bucket:
    """해시를 구성하는 버킷 """
    # stat의 Default = Status.EMPTY
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        """Init"""
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """Buekct의 모든 Field의 값을 설정"""
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        """Bucket의 stat을 설정"""
        self.stat = stat


class OpenHash:
    """Open Addressing으로 구현하는 Hash Class"""

    def __init__(self, capacity: int) -> None:
        """Init"""
        self.capacity = capacity  # Hash Table의 크기 지정
        self.table = [Bucket()] * self.capacity  # Hash Table(List)을 선언

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        """재해시 값을 연산"""
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """키가 key인 Bucket을 검색"""
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # 재해시를 하고 다음 hash값을 가져온다.
            p = self.table[hash]  # 재홰시한 값을 기준으로 hash table의 Field를 가져온다.
        return None

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        if self.search(key) is not None:
            return False

        hash = self.hash_value(key)  # 해시 함수를 이용해 key 값을 해시값으로 변경한 int값
        p = self.table[hash]  # int 해시값을 기준으로 table의 index를 설정한다.
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        p = self.search_node(key)
        if p is None:  # Buekct의 Value가 존재하지 않기 때문에 False
            return False
        p.set_status(Status.DELETED)  # Bucket의 상태를 DELETED로 변경하며 Value를 읽을 수 없도록 설정
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--EMPTY--')
            elif self.table[i].stat == Status.DELETED:
                print('--DELETED--')


if __name__ == '__main__':
    hash = OpenHash(13)
    hash.add(23, 'Python')
    hash.add(24, 'Js')
    hash.add(25, 'C++')
    hash.add(36, 'Flask')
    hash.add(37, 'Express')
    hash.add(38, 'Win32api')
    hash.remove(23)
    print(hash.search(99))
    print(hash.search(24))
    print(hash.search(25))
    hash.dump()
