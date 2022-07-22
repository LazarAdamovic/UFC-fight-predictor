import scrapy

class FighterSpider(scrapy.Spider):
    name = 'fighters'
    start_urls = ['https://www.fightmetric.com/fighters']

    def parse(self, response):
        for fighter in response.css('div.fighter-list-item'):
            yield {
                'name': fighter.css('div.fighter-list-item-name::text').get(),
                'link': fighter.css('div.fighter-list-item-name a::attr(href)').get(),
                'image': fighter.css('div.fighter-list-item-image img::attr(src)').get(),
                'country': fighter.css('div.fighter-list-item-country::text').get(),
                'height': fighter.css('div.fighter-list-item-height::text').get(),
                'weight': fighter.css('div.fighter-list-item-weight::text').get(),
                'reach': fighter.css('div.fighter-list-item-reach::text').get(),
                'style': fighter.css('div.fighter-list-item-style::text').get(),
                'record': fighter.css('div.fighter-list-item-record::text').get(),
                'bio': fighter.css('div.fighter-list-item-bio::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)