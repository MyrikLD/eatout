# -*- coding: utf-8 -*-

from scrapy import Field, Item
from scrapy.loader.processors import TakeFirst


class EatoutItem(Item):
	# define the fields for your item here like:
	name = Field(output_processor=TakeFirst())
	city = Field(output_processor=TakeFirst())
	addr = Field(output_processor=TakeFirst())
