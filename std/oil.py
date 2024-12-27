from dataclasses import dataclass
from collections import namedtuple, deque
from std.libs.rands import *
import threading
from ctypes import memset, memmove
from sys import getsizeof as sizebytes
from functools import lru_cache 
from multiprocessing import Process as parallel
# from ctypes import c_longlong as bigbig, c_bool as BooleanValue, c_buffer as buffer, c_byte as byte, c_int16 as i16, c_int32 as i32, c_int64 as i64, c_long as bign, c_short as small, c_double as doublef, c_uint as unsigned, c_uint32 as u32, c_uint16 as u16, c_uint64 as i64, c_ubyte as ubyte, c_char as char, c_char_p as pointchar, c_float as floath, c_int as inth, c_int8 as i8, c_longdouble as bigdouble, c_size_t as usize, c_ssize_t as size, c_uint8 as u8, c_ulong as unsignedbig, c_ulonglong as unsignedbigbig, c_ushort as unsignedsmall, c_wchar as longc, c_wchar_p as pointerlongc, c_void_p as voidh, c_time_t as timeh, create_string_buffer as strbuff  

statich = {}

def clamp(value, minimum, maximum):
    return max(min(value, maximum), minimum)

def struct(args):
    return namedtuple(f"Struct", args)

class String(str):
    def __call__(self):
        return list(self)
    
def clone(iters):
    return [iters,iters]

# class thread:
#     def __init__(self, function, arguments):
#         self.thread = threading.Thread(target=function, args=arguments)

#     def __call__(self):
#         print("e1", self.thread)
#         self.thread.start()

#     def end(self):
#         self.thread.join()



class Ordinator:
    def __init__(self):
        self._data = {}
        self._key_map = {}

    def add(self, keys, value):
        """
        Adds a value associated with multiple keys.

        :param keys: A list or set of keys.
        :param value: The value to associate with the keys.
        """
        if not isinstance(keys, (list, set, tuple)):
            raise TypeError("Keys must be a list, set, or tuple.")

        # Store the value
        value_id = id(value)
        self._data[value_id] = value

        # Map each key to the value's ID
        for key in keys:
            self._key_map[key] = value_id

    def get(self, key):
        """
        Retrieves the value associated with a key.

        :param key: The key to look up.
        :return: The associated value or None if the key does not exist.
        """
        value_id = self._key_map.get(key)
        if value_id is None:
            return None
        return self._data[value_id]

    def remove_key(self, key):
        """
        Removes a single key from the dictionary.

        :param key: The key to remove.
        """
        if key in self._key_map:
            del self._key_map[key]

    def remove_value(self, value):
        """
        Removes all keys associated with a value.

        :param value: The value to remove.
        """
        value_id = id(value)
        keys_to_remove = [key for key, vid in self._key_map.items() if vid == value_id]

        for key in keys_to_remove:
            del self._key_map[key]

        if value_id in self._data:
            del self._data[value_id]

    def keys(self):
        """
        Returns all keys in the dictionary.

        :return: A list of keys.
        """
        return list(self._key_map.keys())

    def values(self):
        """
        Returns all unique values in the dictionary.

        :return: A list of values.
        """
        return list(self._data.values())

    def __repr__(self):
        return f"MultiKeyDictionary({{key: self.get(key) for key in self.keys()}})"

class queue(deque):
    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        return self.popleft()

def flatten(matrix):
    return [item for sublist in matrix for item in sublist]

def index_sub(text, substring):
    return [i for i in range(len(text)) if text.startswith(substring, i)]

OILVARS = vars()