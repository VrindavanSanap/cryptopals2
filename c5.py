#!/usr/bin/python3
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from string import ascii_lowercase, ascii_uppercase

from c2 import bxor


def repeat_key_xor(message, key):
  b_message = bytes(message, encoding='utf-8')
  b_key = bytes(key, encoding="utf-8")
  keystream = b_key*(len(b_message) // len(b_key) + 1)
  res = bxor(b_message, keystream)
  return res
if __name__ == "__main__":
  message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
  key = "ICE" 
  res = repeat_key_xor(message, key)
  print(f"message: {message}")
  print(f"key: {key}")
  print(f"res: {hexlify(res)}")
