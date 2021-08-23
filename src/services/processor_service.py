__all__ = [
    "ProcessorService",
    "get_proc_service",
]

from typing import List, Optional

from src.models import ProcessorRepo, get_proc_repo, ProcessorModel


class ProcessorService:
    """
    Services forward parameters from facade to repos/data models and get, filter, manipulate data.
    At this level, class should know about data from sources, and input parameters from facade.
    """

    def __init__(self, proc_repo: ProcessorRepo):
        self._proc_repo = proc_repo

    def get_all_cpus(self) -> List[ProcessorModel]:
        return self._proc_repo.get_all()

    def create_new_cpu(self, name: str, cores: int, threads: int) -> ProcessorModel:
        return self._proc_repo.add_new_proc(name, cores, threads)

    def filter_by_cores(self, min_cores: int, max_cores: int) -> Optional[List[ProcessorModel]]:
        return self._proc_repo.filter_by_cores(min_cores, max_cores)

    def filter_by_threads(self, min_thr: int, max_thr: int) -> Optional[List[ProcessorModel]]:
        return self._proc_repo.filter_by_threads(min_thr, max_thr)


def get_proc_service() -> ProcessorService:
    """
    Service can be inited with additional sources of data, like ApiClass, parsers, caches, another db, etc.
    :return:
    """
    return ProcessorService(proc_repo=get_proc_repo())
