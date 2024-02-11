#!/usr/bin/python3

import numpy as np
np.set_printoptions(precision=2)

from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from string import ascii_lowercase, ascii_uppercase

from c2 import bxor

expected_prob = np.array([0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507,0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360,0.00150, 0.01974, 0.00074])
chars = "abcdefghijklmnopqrstuvwxyz"

assert len(chars) == 26

stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}


def chi_squared(expected, observed):
  expected = np.array(expected)
  observed = np.array(observed)

  return ((observed - expected)**2 / expected).sum()

def word_freq(string):
  """
  given a string return frequencies as a list 
  """
  frequencies = np.zeros(26)
  for char in string:
    if 'a' <= char <= 'z' and char.isalpha():
      char = char.lower()
      index = ord(char) - ord('a')
      frequencies[index] += 1
  return frequencies

def sentence_chi_squared(sentence):
  length = len(sentence)
  expected_freq = expected_prob * length
  chi_squared_score = chi_squared(expected_freq, word_freq(sentence))
  return chi_squared_score


all_char = (ascii_lowercase + ascii_uppercase)

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
byte_string1 = unhexlify(hex_string)


for c in all_char: 
  byte_string2 = bytes(c, encoding='utf8') * len(byte_string1)
  res =  bxor(byte_string1, byte_string2)
  res_str = res.decode(encoding='utf-8', errors='strict')
  score = sentence_chi_squared(res_str) 
  print(f"{c} --> {res} score = {score:.2f}")
