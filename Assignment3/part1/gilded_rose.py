# -*- coding: utf-8 -*-

#--------------------GLOBAL CONSTANTS--------------------#
#TODO Global Constants, min, max values, passed sell-by-date (possible others)


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

    # TODO - helper function to select appropriate item to update???
    """
    Pseudo for new update_quality function to select an item to update:
    
    def update_quality(self):
        for an item in items:
            if item == Aged Brie
                update item aged brie
            else if item == Backstage passes to a TAFKAL80ETC concert
                update Backstage passes to a TAFKAL80ETC concert
            else if item == Conjured Mana Cake
                update item Conjured Mana Cake
            else item == Sulfas, Hand of Ragnaros
                update item Sulfas, Hand of Ragnaros        
    """

    # --------------------ORIGINAL CODE--------------------#
    # def update_quality(self):
    #     for item in self.items:

              #item quality
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0: #min number (item quality more than 0, do the below)
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1

    #         else:
    #             if item.quality < 50: #max number (item quality less than 50, do the below)
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1

              #item sell-by-date
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1 #passed_sell (if the item date is -1, do the below)
    #
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 #decrement item quality if Mana Cake
    #                 else:
    #                     item.quality = item.quality - item.quality
                  #else increment other items by 1 until max (50) reached
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1

# --------------------CLASS (REFACTORED)--------------------#
#TODO - class update
#Needs helper functions (in the GildedRose class???) to select appropriate item to change the appropriate values.

"""
Create class to update/modified functionality (also improves scalability/longevity)

Class needs to have functions for each of the four items (Aged Brie, Backstage passes to a TAFKAL80ETC concert, Conjured Mana Cake, and Sulfuras, Hand of Ragnaros).

Global constants will be needed (See #TODO Global Constants)

Things to note:
- All items have a SellIn value which denotes the number of days we have to sell the item
- All items have a Quality value which denotes how valuable the item is
* At the end of each day our system lowers both values for every item

Additional things to note:
* Once the sell by date has passed, Quality degrades TWICE as fast (double degradation)
- The Quality of an item is never negative (min)
* "Aged Brie" actually increases in Quality the older it gets (Brie is the only item to increase in quality)
- The Quality of an item is NEVER MORE THAN 50 (max)
* "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
--Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
--Quality drops to 0 after the concert

Lastly:
- "Conjured" items degrade in Quality twice as fast as normal items

Function Aged Brie:
increase in quality the older it gets until


Function Backstage passes to a TAFKAL80ETC concert:
increases in quality **increase DOUBLES when the are 10 to 6 days AND TRIPLES when there are 5 or less days and is 0 AFTER date** the older it gets

 
Function Conjured Mana Cake
degrade in quality TWICE as fast as NORMAL items


Function Sulfuras, Hand of Ragnaros:
does not have a sell-by-date AND does not degrade!!! 
no need for any changes here, just pass it


"""



