import scrapy

class fighterspider(scrapy.Spider):
    name = 'fighters'
    start_urls= ['http://www.ufcstats.com/fighter-details/bf0e700106d00e55']
    
    def parse(self, response):
        
        name = response.css('span.b-content__title-highlight::text').get().strip()
        win_loss_tie = response.css('span.b-content__title-highlight::text').get().strip()
        
        lst= response.css('li.b-list__box-list-item_type_block::text').getall()
        lst = [s.strip() for s in lst]
        
    
        yield {
            'name': name,
            'win_loss_tie': win_loss_tie,
            'height_ft': lst[1],
            'weight_lbs': lst[3].replace('lbs', ''),
            'reach_inch': lst[5],
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
