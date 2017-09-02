import re

from scrapy import Request
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from ..items import EatoutItem


class BlogSpider(CrawlSpider):
	name = 'eatout'
	allowed_domains = ['eatout.ru']
	rules = [
		Rule(LxmlLinkExtractor(allow=('\?page=\d+')), callback='get_page', follow=True)
	]
	regex = re.compile('eatout\.ru\/([^\/]*)\/')

	def __init__(self, targets=None, *args, **kwargs):
		super(BlogSpider, self).__init__(*args, **kwargs)
		if targets:
			if ',' in targets:
				self.targets = targets.split(',')
			else:
				self.targets = [targets]
		else:
			self.targets = ['msk', 'spb', 'sochi', 'n-novgorod', 'ekaterinburg', 'omsk', 'kazan']

		self.start_urls = ['https://eatout.ru/%s/search/' % i for i in self.targets]

	def get_page(self, response):
		next_pages = response.xpath("//a[@class='restaurant-item__card']/@href").extract()
		for i in next_pages:
			page = response.urljoin(i)
			yield Request(page, callback=self.get_item)

	def get_item(self, response):
		url = response.url
		city = self.regex.search(url).group(1)
		loader = ItemLoader(EatoutItem(), response)
		loader.add_xpath("name", "//h1[contains(@class, 'company__name')]/text()")
		loader.add_xpath("addr", "//span[contains(@class, 'company__address-text')]/text()")
		loader.add_value("city", city)
		item = loader.load_item()
		return item
