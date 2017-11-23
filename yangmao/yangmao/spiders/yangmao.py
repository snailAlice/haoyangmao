#-*- coding : utf -8 -*-
__author__ = 'wangxiangyang'
#created by 2017.11.21
import os
import scrapy
import requests
from bs4 import BeautifulSoup
from ..items import YangmaoItem

class Yangmao(scrapy.Spider):
    name = 'yangmao'
    #start crawler urls
    start_urls = ['https://www.haoyangmao8.com/page_{}.html'.format(i) for i in range(2,50)]

    #start parser
    def parse(self, response):
        result = response.xpath('//*[@id="kuangjia"]/div[2]/div/div[1]/div[@class="firstreed"]')
        item = YangmaoItem()

        #The results of the first analysis for further analysis, extracted useful information on the field
        for point1 in result:
            #Analyze the title of the article
            item['title'] = point1.xpath('div[@class="reed"]/h2/a/text()').extract_first()
            #Analyze the tags of the article
            item['category_id'] = point1.xpath('div[@class="reed"]/h6/a[2]/text()').extract_first()

            #get the text corresponding to the article URL
            item['link_url'] = point1.xpath('div[@class="reed"]/h2/a/@href').extract_first()

            #The text of the article request, analysis of the contents of the article
            r = requests.get(item['link_url'])
            soup = BeautifulSoup(r.content,'lxml')
            neirong = soup.find('dd').find_all_next('p')
            content = ''
            #Polls iterate out of the article content, save to a string variable
            content = ''
            for part in neirong:
                content = content + str(part)
            item['content'] = content
            yield item














