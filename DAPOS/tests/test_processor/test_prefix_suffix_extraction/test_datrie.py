# -*- coding: UTF-8 -*-
'''
This module is not for test, but to give a try of the usage of
detrie lib and to help test the api we will use against thier change!
'''
import unittest
import datrie

arabic_chars = u'اآأإبتثجحخدذرزسشصضظعغفقكلمنهوؤيىًٌٍَُِّْ'


class TestDatrie(unittest.TestCase):
    """datrie is a c impelentation for trie algorithm, wrapped for/in python"""
    def test_basic_functionalities(self):
        trie = datrie.Trie(arabic_chars)
        trie[u'ا'] = 1
        trie[u'است'] = 1
        trie[u'ت'] = 2
        trie[u'ات'] = 1
        trie[u'مت'] = 1

        self.assertEqual(set([u'است', u'ا']), set(trie.prefixes(u'استطيع')))
        self.assertEqual(set([u'مت',]), set(trie.prefixes(u'متكتب')))
        self.assertEqual(set([u'ت',]), set(trie.prefixes(u'تكتب')))
        self.assertEqual(set([u'ا',]), set(trie.prefixes(u'اكتب')))
        self.assertEqual(set([u'ا', u'ات']), set(trie.prefixes(u'اتكتب')))

        trie.save('prefixes.trie')
        trie2 = datrie.Trie.load('prefixes.trie')

        self.assertEqual(trie.items(), trie2.items())
