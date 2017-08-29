# -*- coding: utf-8 -*-
import json

from os import path

class EatoutPipeline(object):
	def process_item(self, item, spider):
		with open('output/'+item['name']+'.json', 'w') as f:
			dump = json.dumps(dict(item), ensure_ascii=False)
			f.write(dump)
		return item
