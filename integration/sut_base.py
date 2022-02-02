# coding=utf-8
"""
==============================================================================
Name:         sut_base.py

Purpose:      test base for integration test cases

Author:       Huck
Created:      2/1/2022

==============================================================================
"""

import unittest
import logging

class SUTBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        logging.basicConfig(
            format='\n%(levelname)s: %(message)s', level=logging.INFO)
