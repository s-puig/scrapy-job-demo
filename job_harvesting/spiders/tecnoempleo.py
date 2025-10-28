import datetime
from typing import AsyncGenerator, Any

import scrapy

from job_harvesting.items.tecnoempleo_scraping_item import TecnoempleoScrapingItem, TecnoempleoExperienceLevel, \
    TecnoempleoContractType, TecnoempleoRemoteStatus


class TecnoempleoSpider(scrapy.Spider):
    name = "tecnoempleo"
    allowed_domains = ["tecnoempleo.com"]
    start_urls = ["https://tecnoempleo.com/ofertas-trabajo/"]

    def parse(self, response: scrapy.http.Response) -> AsyncGenerator[scrapy.http.Request, None]:
        # Go to offer page
        offers = response.xpath('//div[@class="container"]/div/div/div/div/div/h3/a/@href').getall()
        yield from response.follow_all(iter(offers), callback=self.parse_offer)

        # Go to next page if it exists
        next_page_link = response.xpath('//a[@class="page-link" and normalize-space(text())="siguiente"]/@href').get()
        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)

    def parse_offer(self, response: scrapy.http.Response) -> AsyncGenerator[TecnoempleoScrapingItem, None]:
        container = response.xpath('//div[@class="container"]')
        header = container.xpath('//div[@class="row"]')
        id = container.xpath('.//input[@name="refer"]/@value').get()
        title = header.xpath('normalize-space(//h1[@itemprop="title"])').get()
        company = header.xpath('normalize-space(//div/a/span[@itemprop="name"])').get()
        date_posted = header.xpath('normalize-space(//i[contains(@class, "fi-calendar")]/parent::span)').get()
        experience_level = TecnoempleoExperienceLevel.from_str(header.xpath('normalize-space(//i[contains(@class, "fi-shield-ok")]/ancestor::li[1]/span)').get())
        contract_type = TecnoempleoContractType.from_str(header.xpath('normalize-space(//i[contains(@class, "fi-task-list")]/ancestor::li[1]/span)').get())
        description = container.xpath('normalize-space(//div[@itemprop="description"]/p)').get()
        yield TecnoempleoScrapingItem(id=id, title=title, company=company, date_posted=date_posted, experience_level=experience_level,contract_type=contract_type, description=description, location=None, province=None, remote_status=TecnoempleoRemoteStatus.UNDEFINED)

    async def start(self) -> AsyncGenerator[scrapy.http.Request, None]:
        tags = getattr(self, "tags", None)
        tags = tags.split(",") if tags else None
        experience = getattr(self, "experience", None)
        #from
        #studies
        #location
        #remote mode (on-site, remote, hybrid)
        #contract type (internship, permanent, freelance, n/d)
        #fulltime/partial/etc
        params = "?"
        if experience:
            params += f"ex={experience}"
        for tag in tags:
            yield scrapy.Request(f"{self.start_urls[0]}{params}&te={tag}", callback=self.parse)