# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobHarvestingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    province = scrapy.Field()
    #salary = scrapy.Field()
    description = scrapy.Field()
    #url = scrapy.Field()
    date_posted = scrapy.Field()
    contract_type = scrapy.Field()
    employment_type = scrapy.Field()
    experience_level = scrapy.Field()
    remote_status = scrapy.Field()
    #posted_by = scrapy.Field()
    pass
    pass
