from job_harvesting.items.job_offer_item import JobOfferItem
from job_harvesting.items.tecnoempleo_scraping_item import TecnoempleoScrapingItem
from job_harvesting.pipelines.tecnoempleo_pipeline import TecnoempleoPipeline


class JobHarvestingDispatcherPipeline:
    def process_item(self, item, spider) -> JobOfferItem:
        if isinstance(item, TecnoempleoScrapingItem):
            return TecnoempleoPipeline().process_item(item, spider)

        raise RuntimeError("Item type not supported: " + str(type(item)) + ". This is caused by a missing pipeline. ")

