# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import re
from scrapy_spider.items import revitem
import logging
logger = logging.getLogger('mycustomlogger')



class BeerspyderSpider(scrapy.Spider):
    name = 'beerspyder'
    allowed_domains = ['beeradvocate.com']
    start_urls = ['https://www.beeradvocate.com/beer/styles/']
    baseurl = 'https://www.beeradvocate.com'
    beerurllist = []
    
    def parse(self, response):
        stylegroups = response.css('div div[class*="stylebreak"]')
        for stylegroup in stylegroups:
            substyles = stylegroup.css('a')
            for substyle in substyles:
                next_url = self.baseurl +substyle.css('a::attr(href)').get()
                self.beerlurllist = []
                yield(scrapy.Request(next_url, callback = self.parse_style))
                
                
                        
    def parse_style(self, response): 
        navurls =response.css('div[id="ba-content"] span a')
        more_beerurl = ''
        beers = response.css('div[id="ba-content"] table tr a[href*="profile"]')
        for i in range(0,len(beers),2):
            self.beerurllist.append(self.baseurl + beers[i].css('::attr(href)').get())  
              
        if any(item == 'next' for item in navurls.css('::text').getall()): 
            more_beerurl = self.baseurl + navurls[navurls.css('::text').getall().index('next')].css('::attr(href)').get()
            yield(scrapy.Request(more_beerurl,callback = self.parse_style))
        else:
            for url in self.beerurllist:
                yield(scrapy.Request(url,callback = self.parse_beer))
      
        
                    
                    
                    
    def parse_beer(self, response):
        item = revitem()
        item['name'] = response.css('h1::text').get()
        
        beerstats = response.css('dl.beerstats')
        item['abv'] =beerstats.css('dd span[title*="alcohol"] ::text').get()
        item['score'] = beerstats.css('dd span[title*="Score"] ::text').get()
        item['avg_rating']=beerstats.css('dd span[title*="mean"] ::text').get()
        item['num_reviews'] = beerstats.css('dd span[title*="reviews"] ::text').get()
        item['num_ratings'] =beerstats.css('dd span[title*="Number of ratings"] ::text').get()
        item['wants'] =beerstats.css('dd span[title*="want"] ::text').get()
        item['gots'] =beerstats.css('dd span[title*="have"] ::text').get()
        item['availability'] =beerstats.css('dd span[title*="availability"] ::text').get()
        item['style'] = beerstats.css('a[title*="Learn"] ::text').get()
        item['brewery'] = beerstats.css('a[title*="brewery"] ::text').get()
        item['location'] =beerstats.css('a[href*="place"] ::text').get()     
        
        revlist = response.css('div[id="rating_fullview_container"]')
        if len(revlist)>0:
            for review in revlist:
                yield(self.parse_review(review,item))
        else:
            yield(item)
            

    
    def parse_review(self,rev,beeritem):
          item=revitem()
          item['name'] = beeritem['name']
          item['abv'] = beeritem['abv']
          item['score'] = beeritem['score']
          item['avg_rating']=beeritem['avg_rating']
          item['num_reviews'] = beeritem['num_reviews']
          item['num_ratings'] =beeritem['num_ratings']
          item['wants'] =beeritem['wants']
          item['gots'] =beeritem['gots']
          item['availability'] =beeritem['availability']
          item['style'] = beeritem['style']
          item['brewery'] = beeritem['brewery']
          item['location'] = beeritem['location']
          item['user_id'] = rev.css('div::attr(ba-user)').get()
          item['ba_score'] = rev.css('span.BAscore_norm::text').get()
          
          ratinglist = rev.css('span.muted::text').getall()
          ratingstring = ''.join(ratinglist)          
          try:
              item['look'] = float(re.findall('look: (.+?) \|',ratingstring)[0])
              item['smell'] = float(re.findall('smell: (.+?) \|',ratingstring)[0])
              item['taste'] = float(re.findall('taste:(.+?) \|',ratingstring)[0])
              item['mouth_feel'] =float(re.findall('feel: (.+?) \|',ratingstring)[0])
              overall = re.findall('overall: (.+?)',ratingstring)[0]
              item['overall'] =float(overall)
          except:
              pass          
          try:
              fulltext = rev.extract().replace('\n','')
              item['text'] = re.findall('</span><br><br>((?!<).+?)<br><br><span',fulltext)[0]
          except:
              pass            
          try:
              item['date'] = rev.css('span.muted a::text').getall()[1]
          except:
              pass  
          return(item)