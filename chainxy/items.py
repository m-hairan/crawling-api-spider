# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ChainItem(Item):

    FrequencyAllCultures = Field()

    FemalePercentAllCultures = Field()

    MalePercentAllCultures = Field()

    AMBIGUOUS_frequency = Field()

    AMBIGUOUS_femalePercent = Field()

    AMBIGUOUS_malePercent = Field()

    ANGLO_femalePercent = Field()

    ANGLO_frequency = Field()

    ANGLO_malePercent = Field()