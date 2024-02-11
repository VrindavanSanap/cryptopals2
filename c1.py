#!/usr/bin/python3

from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_b64(hex_string):
  byte_form = unhexlify(hex_string)
  base64_form = b64encode(byte_form)
  return base64_form 

if __name__ == '__main__':
  print(f"byte form: {unhexlify(hex_string)}")
  print(f"base64 form: {hex_to_b64(hex_string)}")
