Parser for `eatout.ru` site 
 ## Usage
 Scan all cities:
 
    scrapy crawl eatout
    
 Scan only one city:
 
 	scrapy crawl eatout -a targets=msk
 	
 Scan list of cities:
 
	scrapy crawl eatout -a targets=msk,spb
