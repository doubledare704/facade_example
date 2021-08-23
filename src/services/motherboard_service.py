__all__ = [
    "MotherBoardService",
    "get_board_service",
]

from typing import List

from src.models import MotherboardRepo, get_mother_repo, MotherboardModel


class MotherBoardService:
    """
    Services forward parameters from facade to repos/data models and get, filter, manipulate data.
    At this level, class should know about data from sources, and input parameters from facade.
    """

    def __init__(self, board_repo: MotherboardRepo):
        self._board_repo = board_repo

    def get_all_boards(self) -> List[MotherboardModel]:
        return self._board_repo.get_all()

    def create_new_board(self, name: str, socket: str, chipset: str) -> MotherboardModel:
        return self._board_repo.add_new_board(name, socket, chipset)


def get_board_service() -> MotherBoardService:
    """
    Service can be inited with additional sources of data, like ApiClass, parsers, caches, another db, etc.
    :return:
    """
    return MotherBoardService(board_repo=get_mother_repo())
