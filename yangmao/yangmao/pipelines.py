# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='wxy',
        passwd='wxy@2017',
        charset='utf8',
        use_unicode=False
    )
    return conn

class YangmaoPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE yangmao")
        sql = 'insert into yangmao_news(title,category_id,link_url,content) values (%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (item['title'],item['category_id'], item['link_url'], item['content']))
            dbObject.commit()
        except Exception, e:
            print ("错误在这里>>>>>>>>>>",e,"<<<<<<<<<<<<<<<<<<")
            dbObject.rollback()

        return item