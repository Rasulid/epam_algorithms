"""
Mutable
    list
    dict
    set
    bytearray
"""

"""
Immutable
    str
    int
    float
    tuple
    byte
    bool
    frozenset
"""

"""
frozen Set

frozenset_create = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})
print(frozenset_create)
frozenset_create[0] = 6  # This line will raise a TypeError

"""
"""
bytes

bytes_binary_literal = b'\x48\x65\x6c\x6c\x6f'  # Represents the ASCII values of 'Hello'
print(bytes_binary_literal)  # Output: b'Hello'
"""

"""
bytearray

>>> greeting = bytearray(b"Hello, World!")

>>> greeting[1] = 69
>>> greeting
bytearray(b'HEllo, World!')

>>> greeting[2] = "L"
Traceback (most recent call last):
    ...
TypeError: 'str' object cannot be interpreted as an integer

>>> greeting[2] = b"L"
Traceback (most recent call last):
    ...
TypeError: 'bytes' object cannot be interpreted as an integer

>>> greeting[2] = bytearray(b"L")
Traceback (most recent call last):
    ...
TypeError: 'bytearray' object cannot be interpreted as an integer

"""