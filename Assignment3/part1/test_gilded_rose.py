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
        item = Item("Aged Brie", 30, 30)
        gilded_rose = GildedRose([item]) # create a GildRose list of items

        # First day
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in,29) # second = sell_in -1
        self.assertEqual(item.quality,31) # second = quality +1

        #TODO
        # Sell-by-date expired (day -1)
        # GildedRose.update_quality(gilded_rose, item.sell_in + 1)
        # self.assertEqual(item.sell_in, -1)

        # 2x quality INCREASE

    """
    Backstage passes to a TAFKAL80ETC concert
    """
    def test_backstage_passes(self):
        # Item instance
        item = Item("Backstage passes to a TAFKAL80ETC concert", 25, 31)
        gilded_rose = GildedRose([item]) # create a GildRose list of items

        # First day
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 24) # second = sell_in -1
        self.assertEqual(item.quality, 32) # second = quality +1
        GildedRoseTest.update_quality(gilded_rose, 9) # updates list

        #TODO
        # 2x for 10 or fewer days
        # 3x for 5 or fewer days
        # Sell-by-date expired (day -1)

    """
    Conjured Mana Cake
    """
    def test_conjured_mana_cake(self):
        # Item instance
        item = Item("Conjured Mana Cake", 5, 0)
        gilded_rose = GildedRose([item]) # create a GildRose list of items

        #TODO
        # First day
        # Sell-by-date expired (day -1)
        # 4x quality DECREASE

    """
    Sulfuras, Hand of Ragnaros
    """
    def test_sulfuras(self):
        # Item instance
        item = Item("Sulfuras, Hand of Ragnaros", 1, 80) # quality should be 80 per spec
        gilded_rose = GildedRose([item]) # create a GildRose list of items

        # First day
        gilded_rose.update_quality()
        self.assertNotEqual(item.sell_in, 19) # second tests sell_in is not the value
        self.assertEqual(item.sell_in, 1) # second = match sell_in
        self.assertEqual(item.quality, 80) # second = match quality

        # Sell-by-date expired (day -1)
        self.assertEqual(item.sell_in, 1) # second = match sell_in
        self.assertNotEqual(item.sell_in, -1) # passed 0

if __name__ == '__main__':
    unittest.main()
