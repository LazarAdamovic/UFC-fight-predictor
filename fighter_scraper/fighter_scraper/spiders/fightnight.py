import scrapy


# http://www.ufcstats.com/statistics/fighters?char=a&page=all

class fightnight(scrapy.Spider):
    name = 'fightnight'
    start_urls=['http://www.ufcstats.com/statistics/events/completed?page=all']
        
    def parse(self, response):
        
        urls = response.css('a.b-link::attr(href)')
        yield from response.follow_all(urls, self.parse)
        
        row = response.css('tr.b-fight-details__table-row.b-fight-details__table-row__hover.js-fight-details-click')  
        # could also ha
        #response.xpath('//table//text()').extract() # supposed to get table details, does, but it's messy and I don't know how to use it
        # response.css('tr.js-fight-details-click').get() #gets the table row, needs to be saved and parsed
        
        
        #def winner_winner_chicken_dinner(x):
        #    if response.css('i.b-flag__text::text').getall() == 'win':

        #event information    
        #win_vs_tie = response.css('i.b-flag__text::text').get()

        #fighter_lst=response.css('a.b-link.b-link_style_black::text').getall()
        
        yield {
        'date': response.css('li.b-list__box-list-item::text')[1].get().strip(),
        'location': response.css('li.b-list__box-list-item::text')[3].get().strip(),
        'poss_winner' : response.css('a.b-link.b-link_style_black::text').get().strip(),
        'poss_loser' : response.css('a.b-link.b-link_style_black::text')[1].get().strip()
         
        }
        