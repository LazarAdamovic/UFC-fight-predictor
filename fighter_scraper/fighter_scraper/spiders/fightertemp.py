import scrapy 

class fighterspider2(scrapy.Spider): # my first spider scrape!
    name = 'fighters2'
    start_urls= ['http://www.ufcstats.com/fighter-details/41e83a89929d1327'] # should be http://www.ufcstats.com/statistics/fighters
    #start url works somehow but not sure how
    
    def parse(self, response):
        
        for link in response.css('a.b-link::attr(href)').getall():
            yield response.follow(link, self.parse) # need to change this one as i keep on getting duplicates. however i can fix it in pandas 
            
            #name
            name = response.css('span.b-content__title-highlight::text').get().strip()
            
            #win/loss/tie record
            win_loss_tie = response.css('span.b-content__title-record::text').get().strip()
            wlt_lst=win_loss_tie.split('-')
            win=wlt_lst[0].replace('Record: ', '')
            loss=wlt_lst[1]
            tie=wlt_lst[2]
            
            #stats
            lst= response.css('li.b-list__box-list-item_type_block::text').getall() # needed to create a list to get the stats
            lst = [s.strip() for s in lst] 
            
            #return fighter stats
            yield { 
                'name': name,
                'win': win,
                'loss': loss,
                'tie': tie,
                'height_ft': lst[1],
                'weight_lbs': lst[3].replace(' lbs.', ''),
                'reach_inch': lst[5].replace('"', ''),
                'stance': lst[7],
                'dob': lst[9],
                'slpm': lst[11],
                'str_acc': lst[13],
                'sapm': lst[15],
                'str_def': lst[17],
                'tdavg': lst[21],
                'tdacc': lst[23],
                'tddef': lst[25],
                'subavg': lst[27],
            }
