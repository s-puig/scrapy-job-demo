from enum import Enum


class ContractType(Enum):
    PERMANENT = "permanent"
    TEMPORAL = "temporal"
    FREELANCE = "freelance"
    INTERNSHIP = "internship"
    OTHER = "other"
    UNDEFINED = "undefined"

    def __str__(self):
        return self.value
