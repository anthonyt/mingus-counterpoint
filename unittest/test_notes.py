#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path = ['../'] + sys.path
import mingus.core.notes as notes
from mingus.core.mt_exceptions import RangeError
import unittest


class test_notes(unittest.TestCase):

    def setUp(self):
        self.base_notes = [
            'C',
            'D',
            'E',
            'F',
            'G',
            'A',
            'B',
            ]
        self.sharps = [x + '#' for x in self.base_notes]
        self.flats = [x + 'b' for x in self.base_notes]
        self.exotic = [x + 'b###b#' for x in self.base_notes]

    def test_base_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x), 'Base notes A-G'),
            self.base_notes))

    def test_sharp_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x), 'Sharp notes A#-G#'
            ), self.sharps))

    def test_flat_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x), 'Flat notes Ab-Gb'),
            self.flats))

    def test_exotic_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x),
            'Exotic notes Ab##b#-Gb###b#'), self.exotic))

    def test_faulty_note_invalidity(self):
        list(map(lambda x: self.assertEqual(False, notes.is_valid_note(x),
            'Faulty notes'), ['asdasd', 'C###f', 'c', 'd', 'E*']))

    def test_valid_int_to_note(self):
        n = [
            'C',
            'C#',
            'D',
            'D#',
            'E',
            'F',
            'F#',
            'G',
            'G#',
            'A',
            'A#',
            'B',
            ]
        list(map(lambda x: self.assertEqual(n[x], notes.int_to_note(x),
            'Int to note mapping %d-%s failed.' % (x, n[x])), list(range(0, 12))))

    def test_invalid_int_to_note(self):
        faulty = [-1, 12, 13, 123123, -123]
        list(map(lambda x: self.assertRaises(RangeError, notes.int_to_note, x),
            faulty))

    def test_to_minor(self):
        known = {
            'C': 'A',
            'E': 'C#',
            'B': 'G#',
            'G': 'E',
            'F': 'D',
            }
        list(map(lambda x: self.assertEqual(known[x], notes.to_minor(x),
            'The minor of %s is not %s, expecting %s' % (x, notes.to_minor(x),
            known[x])), list(known.keys())))

    def test_to_major(self):
        known = {
            'C': 'Eb',
            'A': 'C',
            'E': 'G',
            'F': 'Ab',
            'D': 'F',
            'B': 'D',
            'B#': 'D#',
            }
        list(map(lambda x: self.assertEqual(known[x], notes.to_major(x),
            'The major of %s is not %s, expecting %s' % (x, notes.to_major(x),
            known[x])), list(known.keys())))

    def test_augment(self):
        known = {
            'C': 'C#',
            'C#': 'C##',
            'Cb': 'C',
            'Cbb': 'Cb',
            }
        list(map(lambda x: self.assertEqual(known[x], notes.augment(x),
            'The augmented note of %s is not %s, expecting %s' % (x,
            notes.augment(x), known[x])), list(known.keys())))

    def test_diminish(self):
        known = {
            'C': 'Cb',
            'C#': 'C',
            'C##': 'C#',
            'Cb': 'Cbb',
            }
        list(map(lambda x: self.assertEqual(known[x], notes.diminish(x),
            'The diminished note of %s is not %s, expecting %s' % (x,
            notes.diminish(x), known[x])), list(known.keys())))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_notes)


