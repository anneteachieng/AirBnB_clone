#!/usr/bin/python3

import unittest
import json
import pep8
import datetime

from modes.user import user
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
	def test_doc_module(self):
		doc = user.__doc__
		self.assertGreater(len(doc), 1)

	def test_pep8_conformance_base_model(self):
		"""Test that models/user.py that will/or conforms to PEP8."""
		pep8style = pep8.StyleGuide(quiet=True)
		result = pep8style.check_files(['models/user.py'])
		self.assertEqual(res.total_errors, 0,
				   "Found code style errors (and warnings).")
		
	def test_pep8_conformance_test_base_model(self):
		"""Test that tests/test_models/test_user.py will/or conforms to PEP8"""
		pep8style = pep8.StyleGuide(quiet=True)
		res = pep8style.check_files(['tests/test_models/test_user.py'])
		self.assertEqual(res.total_errors, 0,
				   "Found code style errors (and warnings).")
		
	def test_doc_constructor(self):
		doc = user.__init__.__doc__
		self.assertGreater(len(doc), 1)

	def test_class(self):
		with self.subTest(msg='Inheritance'):
			self.assertTrue(issubclass(user, BaseModel))

		with self.subTest(msg='Attributes'):
			self.assertIsInstance(user.email, str)
			self.assertIsInstance(user.password, str)
			self.assertIsInstance(user.first_name, str)
			self.assertIsInstance(user.last_name, str)

if __name__ == '__main__':
	unittest.main()

