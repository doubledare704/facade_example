__all__ = [
    "MotherboardModel",
    "MotherboardRepo",
    "get_mother_repo",
]

from dataclasses import dataclass
from typing import List

global_motherboard = []


@dataclass
class MotherboardModel:
    name: str
    socket: str
    chipset: str


class MotherboardRepo:
    """
    The source of data for services, methods are used only by services.
    At this layer, class doesn't know about facades and only does work related to data.
    CRUD queries, filtering, deletion are made here.
    """

    def add_new_board(self, name: str, socket: str, chipset: str) -> MotherboardModel:
        board = MotherboardModel(
            name=name,
            socket=socket,
            chipset=chipset,
        )
        global_motherboard.append(board)
        return board

    def get_all(self) -> List[MotherboardModel]:
        return global_motherboard


def get_mother_repo() -> MotherboardRepo:
    return MotherboardRepo()
