__all__ = [
    "MainFacade",
    "get_main_facade",
]

import logging
from typing import List

from src.dtos import ComputerDto
from src.services import ProcessorService, MotherBoardService, GpuService, get_proc_service, get_board_service, \
    get_gpu_service


class MainFacade:
    """
    Main purpose of facade is to combine logic from all services and output results in shorter code.
    In ideal situation facade shouldn't return any model objects, just json or composed objects like Pydantic models
    """

    def __init__(
            self,
            proc_service: ProcessorService,
            mother_board_service: MotherBoardService,
            gpu_service: GpuService,
    ) -> None:
        self._gpu_service = gpu_service
        self._mother_board_service = mother_board_service
        self._proc_service = proc_service

    def create_computer(self, comp_dto: ComputerDto) -> None:
        cpu = self._proc_service.create_new_cpu(
            name=comp_dto.cpu_name,
            cores=comp_dto.cpu_cores,
            threads=comp_dto.cpu_threads,
        )
        motherboard = self._mother_board_service.create_new_board(
            name=comp_dto.board_name,
            socket=comp_dto.board_socket,
            chipset=comp_dto.board_chipset,
        )
        gpu = self._gpu_service.create_new_gpu(
            name=comp_dto.gpu_name,
            type_of_memory=comp_dto.gpu_type_of_memory,
            video_memory_amount=comp_dto.gpu_video_memory_amount,
        )
        logging.warning(f"Created cpu: {cpu}")
        logging.warning(f"Created motherboard: {motherboard}")
        logging.warning(f"Created gpu: {gpu}")

    def get_all_pc_parts(self) -> List:
        res = []
        cpus = self._proc_service.get_all_cpus()
        motherboard = self._mother_board_service.get_all_boards()
        gpus = self._gpu_service.get_all_gpus()

        res.extend(cpus)
        res.extend(motherboard)
        res.extend(gpus)

        return res


def get_main_facade() -> MainFacade:
    return MainFacade(
        proc_service=get_proc_service(),
        mother_board_service=get_board_service(),
        gpu_service=get_gpu_service(),
    )
