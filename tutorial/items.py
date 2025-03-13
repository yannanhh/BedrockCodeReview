# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class YyItem(scrapy.Item):
    author_nickname = scrapy.Field()
    # data_anchor means anchor's id like "407780327"
    data_anchor = scrapy.Field()
    # data_puid means anchor's uid like "74831db68ac07e2fd824988e73acf28e"
    data_puid = scrapy.Field()
    data_videofrom = scrapy.Field()
    data_pid = scrapy.Field()
    data_oid = scrapy.Field()
    data_ouid = scrapy.Field()
    data_yyNo = scrapy.Field()
    v_thumb_img = scrapy.Field()
    v_word_cut = scrapy.Field()
    v_play_times = scrapy.Field()
    v_duration = scrapy.Field()
    v_feedId = scrapy.Field()
    
    def get_record(self):
        """ return the record as tuple """
        return (self['data_puid'], self['data_videofrom'],
                self['data_pid'], self['data_ouid'],
                self['v_thumb_img'], self['v_word_cut'],
                self['v_play_times'], self['v_duration'])
    
    def get_ex_record(self):
        """ return the extend record as tuple """
        return ( self['data_pid'], self['data_anchor'],
                 self['data_yyNo'], self['data_oid'], 
                 self['data_ouid'],  self['v_thumb_img'], 
                 self['v_play_times'], self['v_duration'] )
                 
    
class ExtendYyItem(scrapy.Item):
    data_anchor = scrapy.Field()
    data_ouid = scrapy.Field()
    data_oid = scrapy.Field()
    data_pid = scrapy.Field()
    data_yyNo = scrapy.Field()
    author_nickname = scrapy.Field()
    v_thumb_img = scrapy.Field()
    v_play_times = scrapy.Field()
    v_duration = scrapy.Field()
    
    def get_record(self):
        """ return the recocrd as tuple """
        return (self['data_anchor'], self['data_ouid'],
                self['data_pid'], self['author_nickname'],
                self['v_thumb_img'], self['v_play_times'],
                self['duration'])