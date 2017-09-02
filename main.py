from scrapy import cmdline

if __name__ == '__main__':
	cmdline.execute("scrapy crawl eatout".split())
	#cmdline.execute("scrapy crawl eatout -a targets=msk".split())
	#cmdline.execute("scrapy crawl eatout -a targets=msk,spb".split())
