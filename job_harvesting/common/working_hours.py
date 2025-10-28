from enum import Enum


class WorkingHours(Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    OTHER = "other"
    UNDEFINED = "undefined"

    def __str__(self):
        return self.value