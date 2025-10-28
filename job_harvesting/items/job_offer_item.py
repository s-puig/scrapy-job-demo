import datetime

import scrapy

from job_harvesting.common.contract_type import ContractType
from job_harvesting.common.remote_status import RemoteStatus
from job_harvesting.common.working_hours import WorkingHours


class JobOfferItem(scrapy.Item):
    title: str = scrapy.Field()
    company: str = scrapy.Field()
    location: str = scrapy.Field()
    province: str = scrapy.Field()
    description: str = scrapy.Field()
    date_posted: datetime.datetime = scrapy.Field()
    contract_type: ContractType = scrapy.Field()
    working_hours: WorkingHours = scrapy.Field()
    experience_level: int = scrapy.Field()
    remote_status: RemoteStatus = scrapy.Field()

