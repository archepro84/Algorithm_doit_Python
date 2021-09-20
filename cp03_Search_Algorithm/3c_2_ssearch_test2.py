from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    for i in range(len(a)):
        if a[i] == key:
            return i
    return False


if __name__ == '__main__':
    print(seq_search([1, 6, 2, 5, 3, 4, 7, 8], 99))
    print(seq_search((4, 7, 5.6, 2, 3.14, 1), 3.14))
    print(seq_search('string', 'n'))
    print(seq_search(['DTS', 'NSNS', 'EEEE', 'Lo', ], 'Lo'))
