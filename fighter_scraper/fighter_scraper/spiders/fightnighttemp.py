# this one doesn't work it's just where I keep extra code that might end up working

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# www.ufcstats.com/event-details/8fd76e1b49c00ae2

class fightnight(CrawlSpider):
    name = 'fightnighttemp'
    allowed_domains = ['ufcstats.com']
    start_urls=['http://www.ufcstats.com/']
    
    rules = (
        Rule(LinkExtractor(allow='event-details'), callback='parse_poo'),
    )
    
    def parse_poo(self, response):  
        
        #event information   
        date=response.css('li.b-list__box-list-item::text')[1].get().strip()  
        location=response.css('li.b-list__box-list-item::text')[3].get().strip()
        
        #fighter_lst=response.css('a.b-link.b-link_style_black::text').getall()
        
        yield {
         'date': date,
         'location': location,   
        }
        
        
           '''
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            '''
            