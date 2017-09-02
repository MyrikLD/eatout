# -*- coding: utf-8 -*-
import json
import os

class EatoutPipeline(object):
	def process_item(self, item, spider):
		dictitem = dict(item)
		city = dictitem.pop('city')

		path = 'output/'+city+'/'+item['name']+'.json'
		directory = os.path.dirname(path)

		dump = json.dumps(dictitem, ensure_ascii=False)

		if not os.path.exists(directory):
			os.makedirs(directory)

		with open(path, 'w') as f:
			f.write(dump)

		return item
