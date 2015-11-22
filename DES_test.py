# Run some test cases to check if text is being encrypted and
# decrypted correctly

import unittest
from DES import encrypt
from DES import decrypt

class DES_test(unittest.TestCase):

	def check(self, key, plaintext, cipher):
		self.assertEqual(cipher, encrypt(plaintext, key))
		self.assertEqual(plaintext, decrypt(cipher, key))

	def test_case1(self):
		"""
		Regular string!
		"""
		key = "gK8nDAw8"
		plaintext = "I am going to grocery store"
		cipher = "3fd8567e4088b18654628a3edf9447c1b6e06db87c40303407cb411c3c2397ad"
		self.check(key, plaintext, cipher);

	def test_case2(self):
		"""
		Space at the end!
		"""
		key = "CuV72sOD"
		plaintext = "I will come late today "
		cipher = "3103db69e9f13912a45e09f12af567e10caf6a08f676885a" 
		self.check(key, plaintext, cipher);

	def test_case3(self):
		"""
		Random String
		"""
		key = "2t5cyfqW"
		plaintext = "0kLllffV7OTR3FFApwVi"
		cipher = "e6aa03d0b049913af5e1d2ee80415205acf45fe8a75914d5"
		self.check(key, plaintext, cipher);

	def test_case4(self):
		"""
		Numerical String
		"""
		key = "0kLllffV"
		plaintext = "84280397903971647788"
		cipher = "45d7cfe5a49a2c1dd07226456827c25abfe5a6395c99540d"
		self.check(key, plaintext, cipher);

	
