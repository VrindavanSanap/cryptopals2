#!/usr/bin/python3
from binascii import unhexlify, hexlify

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"

def bxor(a, b):
  return bytes([ x^y for (x,y) in zip(a, b)])

res = bxor(unhexlify(str1), unhexlify(str2))

if __name__ == '__main__':

  print(f"str1: {str1}")
  print(f"str2: {str2}")
  print(f"res: {res}")
  print(f"res hex: {hexlify(res)}")
