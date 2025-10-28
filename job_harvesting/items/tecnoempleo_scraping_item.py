import logging
from enum import auto, Enum
from typing import Optional

import scrapy

from job_harvesting.common.contract_type import ContractType
from job_harvesting.common.remote_status import RemoteStatus
from job_harvesting.items.job_offer_item import JobOfferItem


class TecnoempleoExperienceLevel(Enum):
    NONE = auto()
    LESS_THAN_ONE_YEAR = auto()
    ONE_YEAR = auto()
    TWO_YEARS = auto()
    THREE_YEARS = auto()
    THREE_TO_FIVE_YEARS = auto()
    MORE_THAN_FIVE_YEARS = auto()
    MORE_THAN_TEN_YEARS = auto()
    UNDEFINED = auto()

    @classmethod
    def from_str(cls, experience: str) -> Optional["TecnoempleoExperienceLevel"]:
        experience = experience.strip().lower()
        # TODO: Order by likelihood
        if experience == "sin experiencia":
            return cls.NONE
        elif experience == "menos de un año":
            return cls.LESS_THAN_ONE_YEAR
        elif experience == "1 año":
            return cls.ONE_YEAR;
        elif experience == "2 años":
            return cls.TWO_YEARS
        elif experience == "3 años":
            return cls.THREE_YEARS
        elif experience == "3-5 años":
            return cls.THREE_TO_FIVE_YEARS
        elif experience == "más de 5 años":
            return cls.MORE_THAN_FIVE_YEARS
        elif experience == "mas de 10 años":
            return cls.MORE_THAN_TEN_YEARS
        logging.warning("Unknown experience level parsing " + experience + " in " + str(cls) + " enum. " +
                      "Returning UNDEFINED. This is likely caused by a change in the website")
        return cls.UNDEFINED

    def into_years(self) -> int:
        if self == self.NONE:
            return 0
        elif self == self.LESS_THAN_ONE_YEAR:
            return 0
        elif self == self.ONE_YEAR:
            return 1
        elif self == self.TWO_YEARS:
            return 2
        elif self == self.THREE_YEARS:
            return 3
        elif self == self.THREE_TO_FIVE_YEARS:
            return 3
        elif self == self.MORE_THAN_FIVE_YEARS:
            return 5
        elif self == self.MORE_THAN_TEN_YEARS:
            return 10

        return -1

class TecnoempleoRemoteStatus(Enum):
    REMOTE = auto()
    # OFFICE = auto()
    HYBRID = auto()
    UNDEFINED = auto()

    def from_str(cls, remote: str) -> "TecnoempleoRemoteStatus":
        remote = remote.strip().lower()
        if remote == "100% en remoto":
            return cls.REMOTE
        ## The option is there, but it is automatically mixed with undefined ones, so i will disable for now
        # elif remote == "presencial":
        #    return cls.OFFICE
        elif remote == "híbrido":
            return cls.HYBRID
        return cls.UNDEFINED

    def into_remote_status(self) -> RemoteStatus:
        if self == self.REMOTE:
            return RemoteStatus.REMOTE
        elif self == self.HYBRID:
            return RemoteStatus.HYBRID

        return RemoteStatus.UNDEFINED


class TecnoempleoContractType(Enum):
    PERMANENT = auto()
    FIXED_TERM = auto()
    FREELANCE = auto()
    INTERNSHIP = auto()
    UNDEFINED = auto()

    @classmethod
    def from_str(cls, contract: str) -> "TecnoempleoContractType":
        contract = contract.strip().lower()
        if contract == "indefinido":
            return cls.PERMANENT
        elif contract == "freelance/autónomo":
            return cls.FREELANCE
        elif contract == "temporal" or contract == "obra o servicio":
            return cls.FIXED_TERM
        elif contract == "prácticas":
            return cls.INTERNSHIP
        logging.warning("Unknown contract type parsing " + contract + " in " + str(cls) + " enum. " +
                      "Returning UNDEFINED. This is likely caused by a change in the website")
        return cls.UNDEFINED

    def into_contract_type(self) -> ContractType:
        if self == self.PERMANENT:
            return ContractType.PERMANENT
        elif self == self.FIXED_TERM:
            return ContractType.TEMPORAL
        elif self == self.FREELANCE:
            return ContractType.FREELANCE
        elif self == self.INTERNSHIP:
            return ContractType.INTERNSHIP

        return ContractType.UNDEFINED

class TecnoempleoScrapingItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    province = scrapy.Field()
    description = scrapy.Field()
    date_posted = scrapy.Field()
    contract_type: TecnoempleoContractType = scrapy.Field()
    experience_level: TecnoempleoExperienceLevel = scrapy.Field()
    remote_status: TecnoempleoRemoteStatus = scrapy.Field()
