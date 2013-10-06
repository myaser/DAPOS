import unittest
from DAPOS.utils.interval_overlap import BoundariesOverlap


class BoundariesTest(unittest.TestCase):
    def test_boundaries(self):
        b1 = BoundariesOverlap([0, 3, 4, 8, 9, 10, 11, 12, 15, 16, 21],
                               [(9, 11)])
        self.assertEqual(list(b1), [0, 3, 4, 8, 9, 11, 12, 15, 16, 21])

        b2 = BoundariesOverlap([0, 3, 4, 8, 9, 10, 11, 12, 15, 16, 21],
                               [(9, 11), (12, 15)])
        self.assertEqual(list(b2), [0, 3, 4, 8, 9, 11, 12, 15, 16, 21])

        b3 = BoundariesOverlap([0, 3, 4, 8, 9, 10, 11, 12, 15, 16, 21],
                               [(9, 11), (12, 16)])
        self.assertEqual(list(b3), [0, 3, 4, 8, 9, 11, 12, 16, 21])
