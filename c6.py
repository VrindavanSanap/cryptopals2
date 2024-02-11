#!/usr/bin/python3
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from string import ascii_lowercase, ascii_uppercase

from c2 import bxor


s1 = "this is a test"
s2 = "wokka wokka!!!"

def hamming_distance(str1, str2):

  b_str1 = bytes(str1, encoding='utf-8')
  b_str2 = bytes(str2, encoding='utf-8')
  return sum(bin(byte).count('1') for byte in bxor(b_str1, b_str2))

print(hamming_distance(s1, s2))
