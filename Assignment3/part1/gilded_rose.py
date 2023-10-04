# -*- coding: utf-8 -*-

#--------------------CLASS (CANNOT BE MODIFIED, BUT CAN BE EXTENDED)--------------------#
class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


#--------------------CLASS (NEEDS TO BE REFACTORED)--------------------#
class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    #--------------------FUNCTIONS--------------------#
    """
    New update_quality function to select an item to appropriately asses the sell_in and quality.
    """
    def update_quality(self):
        update_item = Update_item()

        for item in self.items:
            if item.name == "Aged Brie":
                update_item.aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                update_item.backstage_passes(item)
            elif item.name == "Conjured Mana Cake":
                update_item.conjured_mana_cake(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                update_item.sulfuras(item)
            else:
                print(">>> Incorrect item <<<")


# --------------------CLASS (REFACTORED)--------------------#
"""
Class to update the sell_in and quality of a specific item.
"""
class Update_item(object):

    #--------------------GLOBAL CONSTANTS--------------------#
    MIN_QUALITY = 0
    MAX_QUALITY = 50
    PAST_DATE = -1
    SINGLE_RATE = 1
    DOUBLE_RATE = 2
    TRIPLE_RATE = 3

    #--------------------FUNCTIONS--------------------#
    """
    Function Aged Brie increases in quality the older it gets until itme quality is 50.
    """
    def aged_brie(self, item):
        if item.sell_in > 0:
            appreciation = self.SINGLE_RATE
        else:
            appreciation = self.DOUBLE_RATE

        item.quality = min((item.quality + appreciation), self.MAX_QUALITY)
        item.sell_in += self.PAST_DATE

    """
    Function Backstage passes to a TAFKAL80ETC concert increases in quality (increase DOUBLES when there are 10 to 6 days AND TRIPLES when there are 5 to 1 days and is 0 AFTER the date) the older it gets until AFTER the date.
    """
    def backstage_passes(self, item):
        """
        Helper function to get the quality based on the day of appreciation.
        :param item: the item (ticket)
        :return: the quality given the day
        """
        def get_quality(item, appreciation):
            item.quality = min(item.quality + appreciation, self.MAX_QUALITY)

            if item.sell_in > 10:
                appreciation = self.SINGLE_RATE
                get_quality(item, appreciation)
            elif item.sell_in > 5:
                appreciation = self.DOUBLE_RATE
                get_quality(item, appreciation)
            elif item.sell_in > 0:
                appreciation = self.TRIPLE_RATE
                get_quality(item, appreciation)
            else:
                item.quality = 0
                item.sell_in += self.PAST_DATE

    """
    Function Conjured Mana Cake decreases in quality TWICE as fast as a NORMAL item.
    """
    def conjured_mana_cake(self, item):
        if item.sell_in > 0:
            depreciation = -2
        else:
            depreciation = -4

        item.quality = max((item.quality + depreciation), self.MIN_QUALITY)
        item.sell_in += self.PAST_DATE

    """
    Function Sulfuras, Hand of Ragnaros DOES NOT have a sell-by-date AND DOES NOT degrade (...no need for any changes, pass it).
    """
    def sulfuras(self, item):
        pass
