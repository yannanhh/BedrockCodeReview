# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log

class TutorialPipeline(object):
    
    def process_item(self, item, spider):
        try:
            with open( item['data_anchor'] + '.txt', 'r') as fp:
                if item['data_pid'] in fp.read().decode('utf8'):
                    return item 
        except IOError as e:
            if e.errno == 2:
                log.msg(item['data_anchor'] + '.txt not be created', level='WARNING')
        with open( item['data_anchor'] + '.txt', 'a+') as fp:
            if item['data_yyNo'] and item['data_pid']:
                fp.write(('|'.join(item.get_ex_record()) + '\n').encode('utf8'))
            else:
                fp.write(('|'.join(item.get_record()) + '\n').encode('utf8'))
        return item
