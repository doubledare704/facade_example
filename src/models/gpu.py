__all__ = [
    "GpuModel",
    "GpuRepo",
    "get_gpu_repo"
]

from dataclasses import dataclass
from typing import List

global_gpu = []


@dataclass
class GpuModel:
    name: str
    type_of_memory: str
    video_memory_amount: int


class GpuRepo:
    """
    The source of data for services, methods are used only by services.
    At this layer, class doesn't know about facades and only does work related to data.
    CRUD queries, filtering, deletion are made here.
    """

    def add_new_gpu(self, name: str, type_of_memory: str, video_memory_amount: int) -> GpuModel:
        gpu = GpuModel(
            name=name,
            type_of_memory=type_of_memory,
            video_memory_amount=video_memory_amount,
        )
        global_gpu.append(gpu)
        return gpu

    def get_all(self) -> List[GpuModel]:
        return global_gpu


def get_gpu_repo() -> GpuRepo:
    return GpuRepo()
