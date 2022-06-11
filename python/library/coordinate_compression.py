#
# https://atcoder.jp/contests/abc213/editorial/2366
#
import unittest

def build_coordinate_compression_dict(lst, offset=0):
    return {x: i + offset for i, x in enumerate(sorted(set(lst)))}


def compress_coordinates(lst, offset=0):
    d = build_coordinate_compression_dict(lst, offset=offset)
    return [d[x] for x in lst]


class CoordinateCompressionTest(unittest.TestCase):
    def test_build_dict(self):
        self.assertEqual({1: 0, 4: 1, 9: 2, 13: 3}, build_coordinate_compression_dict([1, 4, 9, 13]))
        self.assertEqual({1: 1, 4: 2, 9: 3, 13: 4}, build_coordinate_compression_dict([1, 4, 9, 13], offset=1))

    def test_compress_coordinates(self):
        self.assertEqual([0, 1, 2, 3, 2, 4], compress_coordinates([12, 21, 31, 99, 31, 102]))
