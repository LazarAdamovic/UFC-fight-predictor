import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class fightnightpandas(scrapy.Spider):
    name = 'fightnightpandas'
    start_urls=['http://www.ufcstats.com/statistics/events/completed?page=all']
    
    custom_settings = {
        'DEPTH_LIMIT': 1
    }
    
    # fetch('http://www.ufcstats.com/event-details/319c15b8aac5bfde')
        
    def parse(self, response):
 
        
        yield from response.follow_all(response.css('a.b-link::attr(href)'), self.parse)

    
        yield {
        'date': response.css('li.b-list__box-list-item::text')[1].get().strip(),
        'location': response.css('li.b-list__box-list-item::text')[3].get().strip(),
        'link' : response.url
            
            }   