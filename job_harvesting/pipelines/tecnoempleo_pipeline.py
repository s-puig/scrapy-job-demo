import scrapy.exceptions

from job_harvesting.items.job_offer_item import JobOfferItem
from job_harvesting.items.tecnoempleo_scraping_item import TecnoempleoScrapingItem
from job_harvesting.spiders.tecnoempleo import TecnoempleoSpider


class TecnoempleoPipeline:
    processed_items = set()

    def process_item(self, item: TecnoempleoScrapingItem, spider: TecnoempleoSpider) -> JobOfferItem:
        if item['id'] in self.processed_items:
            raise scrapy.exceptions.DropItem("Duplicate item: %s" % item.id)
        self.processed_items.add(item['id'])

        return JobOfferItem(
            title=item['title'],
            company=item['company'],
            location=item['location'],
            province=item['province'],
            date_posted=item['date_posted'],
            experience_level=item['experience_level'].into_years(),
            contract_type=item['contract_type'].into_contract_type(),
            description=item['description'],
            remote_status=item['remote_status'].into_remote_status(),
        )