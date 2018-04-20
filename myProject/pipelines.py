# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import datetime

class MyProjectPipeline(object):
    def __init__(self):
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = '/tmp/data'+nowTime+'.json';
        self.file = codecs.open(filename, mode='wb', encoding='utf-8')#数据存储到data.json

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))

        return item
