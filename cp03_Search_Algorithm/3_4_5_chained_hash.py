from __future__ import annotations

import hashlib
from typing import Any


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
        """Init"""
        self.capacity = capacity  # Hash Table의 크기 지정
        self.table = [None] * self.capacity  # Hash Table(List)을 선언

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next  # 다음 노드를 검색한다.

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)  # 해시 함수를 이용해 key 값을 해시값으로 변경한 int값
        p = self.table[hash]  # int 해시값을 기준으로 table의 index를 설정한다.

        while p is not None:  # self.table인 해시 테이블의 단일 연결 리스트 데이터가 없을 때 까지 Loop 한다.
            if p.key == key:
                return False
            p = p.next

        # 가장 최근에 들어온 Data를 table의 다음 객체로 넣음으로 해시 테이블과 가까울 수록 최근 데이터 인것을 확인할 수 있음
        add_node = Node(key, value, self.table[hash]) 
        self.table[hash] = add_node  # 노드를 추가
        return True

    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' > {p.key} ({p.value})', end='')
                p = p.next
            print()


if __name__ == '__main__':
    hash = ChainedHash(13)
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
