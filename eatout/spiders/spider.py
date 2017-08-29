from scrapy import Request
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from ..items import EatoutItem


class BlogSpider(CrawlSpider):
	name = 'eatout'
	start_urls = ['https://eatout.ru/msk/search/']
	allowed_domains = ['eatout.ru']
	rules = [
		Rule(LxmlLinkExtractor(allow=('\?page=\d+')), callback='get_page', follow=True)
	]

	def get_page(self, response):
		next_pages = response.xpath("//a[@class='restaurant-item__card']/@href").extract()
		for i in next_pages:
			page = response.urljoin(i)
			yield Request(page, callback=self.get_item)

	def get_item(self, response):
		loader = ItemLoader(EatoutItem(), response)
		loader.add_xpath("name", "//h1[contains(@class, 'company__name')]/text()")
		loader.add_xpath("addr", "//span[contains(@class, 'company__address-text')]/text()")
		item = loader.load_item()
		return item
