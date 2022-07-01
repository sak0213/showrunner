from abc import ABC, abstractmethod
from typing import Iterable
from entries import Event

class Venue(ABC):
    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def get_events(self) -> Iterable[Event]:
        pass

    def get_response(self):
        pass