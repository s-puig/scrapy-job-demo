from enum import Enum


class RemoteStatus(Enum):
    REMOTE = "remote"
    OFFICE = "office"
    HYBRID = "hybrid"
    UNDEFINED = "undefined"

    def __str__(self):
        return self.value