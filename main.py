import sqlite3
from typing import Dict, Union, Tuple
from PyQt5.QtCore import *


class Alarm:
    def __init__(self, id, name, opis_vkusa, price, volume, type_id) -> None:
        self._id: int = id
        self._name: str = name
        self._opis_vkusa: str = opis_vkusa
        self._price: str = price
        self._volume: int = volume
        self._type_id: int = type_id

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def opis_vkusa(self) -> str:
        return self._opis_vkusa

    @property
    def price(self) -> int:
        return self._price

    @property
    def volume(self) -> int:
        return self._volume

    @property
    def type_id(self) -> int:
        return self._type_id
