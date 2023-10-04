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

    # --------------------EDGE-CASE TEST--------------------#
    """
    Function to update quality over time.
    """
    def update_quality(obj = GildedRose, times = 1):
        for i in range(times):
            obj.update_quality()

    """
    Aged Brie
    """
    def test_aged_brie(self):
        # Item instance
        item = Item("Aged Brie", 1, 30)
        gilded_rose = GildedRose([item])

        # First day
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in,0)
        self.assertEqual(item.quality,31)

        # Sell-by-date expired (day -1)
        GildedRose.update_quality(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, -1)


        # 2x quality INCREASE

    """
    Backstage passes to a TAFKAL80ETC concert
    """
    # Item instance
    # First day
    # 2x for 10 or fewer days
    # 3x for 5 or fewer days
    # Sell-by-date expired (day -1)

    """
    Conjured Mana Cake
    """
    # Item instance
    # First day
    # Sell-by-date expired (day -1)
    # 4x quality DECREASE

    """
    Sulfuras, Hand of Ragnaros
    """
    # Item instance
    # First day
    # Sell-by-date expired (day -1)

if __name__ == '__main__':
    unittest.main()
