__all__ = [
    "GpuService",
    "get_gpu_service",
]

from typing import List

from src.models import GpuRepo, get_gpu_repo, GpuModel


class GpuService:
    """
    Services forward parameters from facade to repos/data models and get, filter, manipulate data.
    At this level, class should know about data from sources, and input parameters from facade.
    """

    def __init__(self, gpu_repo: GpuRepo):
        self._gpu_repo = gpu_repo

    def get_all_gpus(self) -> List[GpuModel]:
        return self._gpu_repo.get_all()

    def create_new_gpu(self, name: str, type_of_memory: str, video_memory_amount: int) -> GpuModel:
        return self._gpu_repo.add_new_gpu(name, type_of_memory, video_memory_amount)


def get_gpu_service() -> GpuService:
    """
    Service can be inited with additional sources of data, like ApiClass, parsers, caches, another db, etc.
    :return:
    """
    return GpuService(gpu_repo=get_gpu_repo())
