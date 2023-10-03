# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    #--------------------DEFAULT TEST--------------------#
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    # --------------------DEFAULT TEST--------------------#
    #TODO - Additional test per item - items need setups like junit testing, edge cases should be tested like day 0 and 50, and when value changes for the concert (10, 5, 0)
    # Aged Brie
    # Backstage passes to a TAFKAL80ETC concert
    # Conjured Mana Cake
    # Sulfuras, Hand of Ragnaros


if __name__ == '__main__':
    unittest.main()
