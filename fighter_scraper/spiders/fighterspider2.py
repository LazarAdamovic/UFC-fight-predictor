import scrapy

class fighterspider2(scrapy.Spider):
    name = 'fighters2'
    start_urls= ['http://www.ufcstats.com/fighter-details/41e83a89929d1327']
    
    def parse(self, response):
        
        #name
        name = response.css('span.b-content__title-highlight::text').get().strip()
        
        #win/loss/tie record
        win_loss_tie = response.css('span.b-content__title-record::text').get().strip()
        wlt_lst=win_loss_tie.split('-')
        win=wlt_lst[0].replace('Record: ', '')
        loss=wlt_lst[1]
        tie=wlt_lst[2]
        
        lst= response.css('li.b-list__box-list-item_type_block::text').getall()
        lst = [s.strip() for s in lst]
        
    
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
