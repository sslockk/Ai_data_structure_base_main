import sys
import ctypes
import struct


a = 42

print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))

# print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))